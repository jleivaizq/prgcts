# -*- coding: utf-8 -*-

from unittest import TestCase

from kihon.graphs import Graph


class GraphTest(TestCase):
    """Simple graph tests"""

    def test_graph_should_be_pretty_printed(self):
        g = Graph(v=['A', 'B', 'C'])
        g.add_edge('A', 'C')

        self.assertEqual("[('A', ['C']), ('B', []), ('C', [])]", g.__str__())

    def test_neighbors_should_be_collected(self):
        g = Graph(v=['A', 'B', 'C', 'D'],
                  e=[('A', ['B', 'C']), ('B', ['D', 'A']), ('C', ['C', 'D']), ('D', ['A', 'B', 'C', 'D'])])

        self.assertEqual(['A', 'B', 'C', 'D'], g.neighbors('D'))

