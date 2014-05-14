def is_bipartite(graph):
    """Check if the given graph is bipartite (2-colorable)"""

    # Set of colored vertexes
    colored = set()

    # Sets of colored vertexes
    colors = [set(), set()]

    # Current color
    current = 0

    # Traverse the graph using depth first search
    for v in graph.traversal(strategy='dfs'):

        #print('{}, red={}, black={}, color={}'.format(v, colors[0], colors[1], 'RB'[current]))

        # Try to color current vertex (if it hasn't been yet)
        if v not in colored:
            colors[current].add(v)
            colored.add(v)
        else:
            current = 0 if v in colors[0] else 1

        # Get the opposite color
        opposite = len(colors) - current - 1

        # Every current vertex's neighbors should be on opposite color
        for n in graph.neighbors(v):

            # Try to color neighbor with opposite color
            if n not in colored:
                colors[opposite].add(n)
                colored.add(n)
            else:
                # If neighbor is in current color, graph is not bipartite
                if n in colors[current]:
                    return False

        # swap colors
        current = opposite

    # graph is bipartite
    return True


