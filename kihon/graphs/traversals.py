# -*- coding: utf-8 -*-
import sys
from abc import ABCMeta, abstractmethod
from collections import deque
import inspect


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

    # TODO: graph is supposed to be connected

    traversal_strategy = 'bfs'

    def traverse(self):
        """Breath First Search implementation"""

        queue = deque()
        visited = set()

        queue.append(self.graph.v[0])

        while queue:

            #print('bfs_queue->{}'.format(queue))

            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph.neighbors(vertex))
                yield vertex


class GraphTraversalDepthFirst(GraphTraversal):

    # TODO: graph is supposed to be connected

    traversal_strategy = 'dfs'

    def traverse(self):
        """Depth First search implementation"""

        stack = []
        visited = set()

        stack.append(self.graph.v[0])

        while stack:

            #print('dfs_stack->{}'.format(stack))

            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.graph.neighbors(vertex))
                yield vertex


traversals = {getattr(klass, 'traversal_strategy'): klass for (_, klass)
              in inspect.getmembers(sys.modules[__name__], inspect.isclass)
              if hasattr(klass, 'traversal_strategy')}