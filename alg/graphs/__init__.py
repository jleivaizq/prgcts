import inspect
import importlib
from collections import defaultdict


class Graph:

    traversals = {getattr(klass, 'traversal_strategy'): klass for (_, klass)
                  in inspect.getmembers(importlib.import_module(__name__ + '.traversals'), inspect.isclass)
                  if hasattr(klass, 'traversal_strategy')}

    def __init__(self, **kwargs):
        self.v = kwargs.get('v', [])
        self.e = defaultdict(list)

        if 'e' in kwargs:
            self.append_edges(kwargs.get('e'))

    def add_vertex(self, vertex):
        self.v.append(vertex)

    def add_edge(self, source, destiny):
        self.e[self.v.index(source)].append(self.v.index(destiny))

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
        if strategy in self.traversals:
            return self.traversals[strategy](graph=self).traverse(**kwargs)
        else:
            raise ValueError('No graph traversal strategy found by the name of {}'.format(strategy))


