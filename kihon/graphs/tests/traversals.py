# -*- coding: utf-8 -*-

from unittest import TestCase

from kihon.graphs import Graph


class GraphTraversalTest(TestCase):
    """Graph traversal tests"""

    def setUp(self):
        self.tree = Graph(v=['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                          e=[('A', ['B', 'C']), ('B', ['D', 'F']), ('E', ['F', 'G'])])

    def test_graph_simple_traversal(self):
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G'], list(self.tree.traversal()))

    def test_graph_bfs_traversal(self):
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G'], list(self.tree.traversal(strategy='bfs')))

    def test_graph_dfs_traversal(self):
        self.assertEqual(['G', 'F', 'E', 'D', 'C', 'B', 'A'], list(self.tree.traversal(strategy='dfs')))
