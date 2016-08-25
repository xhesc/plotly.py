"""
test__jupyter

"""
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

from unittest import TestCase
from os import path, environ
import subprocess

PATH_ROOT = path.dirname(__file__)
PATH_FIXTURES = path.join(PATH_ROOT, 'fixtures')
PATH_TEST_NB = path.join(PATH_FIXTURES, 'test.ipynb')
PATH_TEST_HTML = path.join(PATH_FIXTURES, 'test.html')


class PlotlyJupyterTestCase(TestCase):
    def setUp(self):
        with open(PATH_TEST_NB, 'r') as f:
            self.nb = nbformat.read(f, as_version=4)

        if 'PYENV_VERSION' in environ:
            kernel_name = environ['PYENV_VERSION']
            self.ep = ExecutePreprocessor(timeout=600, kernel_name=kernel_name)
        else:
            self.ep = ExecutePreprocessor(timeout=600)

        self.html_exporter = HTMLExporter()

        self.ep.preprocess(self.nb, {'metadata': {'path': '.'}})
        (self.body, _) = self.html_exporter.from_notebook_node(self.nb)

        with open(PATH_TEST_HTML, 'w') as f:
            f.write(self.body)

    def test_one(self):
        proc = subprocess.Popen(['npm', 'test'],
                                cwd=PATH_ROOT,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        (_, stderr) = proc.communicate()

        if stderr:
            self.fail('One or more javascript test failed')
