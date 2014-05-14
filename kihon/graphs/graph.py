# -*- coding: utf-8 -*-

from collections import defaultdict
from .algorithms import is_bipartite
from .traversals import traversals


class Graph:

    DIRECTED = 0
    UNDIRECTED = 1

    def __init__(self, **kwargs):
        self.v = kwargs.get('v', [])
        self.e = defaultdict(list)
        self.kind = kwargs.get('kind', Graph.DIRECTED)

        if 'e' in kwargs:
            self.append_edges(kwargs.get('e'))

    def add_vertex(self, vertex):
        self.v.append(vertex)

    def add_edge(self, source, dest):

        if source not in self.v:
            self.add_vertex(source)

        if dest not in self.v:
            self.add_vertex(dest)

        self.e[self.v.index(source)].append(self.v.index(dest))

        if self.kind == Graph.UNDIRECTED:
            self.e[self.v.index(dest)].append(self.v.index(source))

    def append_edges(self, edges):
        for (v, edges) in edges:
            for e in edges:
                self.add_edge(v, e)

    def neighbors(self, vertex):
        if vertex in self.v:
            index = self.v.index(vertex)
            return [self.v[x] for x in self.e[index]]

    def items(self):
        return [(v, [self.v[x] for x in self.e[self.v.index(v)]]) for v in self.v]

    def __str__(self):
        return str(self.items())

    def traversal(self, strategy='simple', **kwargs):
        if strategy in traversals:
            return traversals[strategy](graph=self).traverse(**kwargs)
        else:
            raise ValueError('No graph traversal strategy found by the name of {}'.format(strategy))

    def is_bipartite(self):
        return is_bipartite(self)