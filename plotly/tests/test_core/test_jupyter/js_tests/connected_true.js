'use strict';

var test = require('../lib/tape-wrapper');

test('should have the correct number of script tags', function(t) {
    t.plan(1);

    var nodes = document.querySelectorAll('script');
    t.equal(nodes.length, 9);
});

test('should not crash browser', function(t) {
    t.plan(1);
    window.onload = function() { t.pass('window onload'); };
});

test('should have one plotly.js graph', function(t) {
    t.plan(1);

    var nodes = document.querySelectorAll('.js-plotly-plot');
    t.equal(nodes.length, 1);
});

test('should link to plotly.js CDN', function(t) {
    t.plan(1);

    var nodes = document.querySelectorAll('script');
    nodes = Array.prototype.slice.call(nodes, 0);

    var results = nodes.filter(function(node) {
        return node.src === 'https://cdn.plot.ly/plotly-latest.min.js';
    });

    t.equal(results.length, 1);
});
