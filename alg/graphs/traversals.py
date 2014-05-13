# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from collections import deque

class GraphTraversal(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        self.graph = kwargs.get('graph', None)

    @abstractmethod
    def traverse(self):
        pass


class GraphTraversalSimple(GraphTraversal):
    traversal_strategy = 'simple'

    def traverse(self):
        for v in self.graph.v:
            yield v


class GraphTraversalBreathFirst(GraphTraversal):
    traversal_strategy = 'bfs'

    def traverse(self):
        """Breath First Search implementation"""

        queue = deque(self.graph.v)
        visited = set()

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph.neighbors(vertex))
                yield vertex


class GraphTraversalDepthFirst(GraphTraversal):
    traversal_strategy = 'dfs'

    def traverse(self):
        """Depth First search implementation"""

        stack = []
        visited = set()

        for v in self.graph.v:
            stack.append(v)

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.graph.neighbors(vertex))
                yield vertex