# -*- coding: utf-8 -*-
from unittest import TestCase
from alg.graphs import Graph


class GraphTest(TestCase):
    def test_graph_should_be_pretty_printed(self):
        g = Graph(v=['A', 'B', 'C'])
        g.add_edge('A', 'C')

        self.assertEqual("[('A', ['C']), ('B', []), ('C', [])]", g.__str__())

    def test_neighbors_should_be_collected(self):
        g = Graph(v=['A', 'B', 'C', 'D'],
                  e=[('A', ['B', 'C']), ('B', ['D', 'A']), ('C', ['C', 'D']), ('D', ['A', 'B', 'C', 'D'])])

        self.assertEqual(['A', 'B', 'C', 'D'], g.neighbors('D'))

    def test_graph_simple_traversal(self):
        g = Graph(v=['A', 'B', 'C', 'D'],
                  e=[('A', ['B', 'C']), ('B', ['D', 'A']), ('C', ['C', 'D']), ('D', ['A', 'B', 'C', 'D'])])

        self.assertEqual(['A', 'B', 'C', 'D'], list(g.traversal()))

    def test_graph_bfs_traversal(self):
        g = Graph(v=['A', 'B', 'C', 'D', 'E', 'F', 'G'], e=[('A', ['B', 'C']), ('B', ['D', 'F']), ('E', ['F', 'G'])])

        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F', 'G'], list(g.traversal(strategy='bfs')))

    def test_graph_dfs_traversal(self):
        g = Graph(v=['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                  e=[('A', ['B', 'C']), ('B', ['D', 'F']), ('E', ['F', 'G'])])

        self.assertEqual(['G', 'F', 'E', 'D', 'C', 'B', 'A'], list(g.traversal(strategy='dfs')))