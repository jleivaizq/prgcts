# -*- coding: utf-8 -*-

from unittest import TestCase

from kihon.graphs import Graph


class GraphAlgorithmTest(TestCase):
    """Simple graph tests"""

    def test_simple_bipartite_graph(self):
        g = Graph(v=['A', 'B'], e=[('A', ['B'])])
        self.assertTrue(g.is_bipartite())

    def test_simple_non_bipartite_graph(self):
        g = Graph(v=['A', 'B', 'C'], e=[('A', ['B']), ('B', ['C']), ('C', ['A'])])
        self.assertFalse(g.is_bipartite())
