import sys
from kihon.graphs import Graph

if __name__ == '__main__':

    cases = int(sys.stdin.readline())

    for i in range(cases):

        edge_number = int(sys.stdin.readline())

        g = Graph(kind=Graph.UNDIRECTED)
        for edge in range(edge_number):
            g.add_edge(*sys.stdin.readline().split())

        sol = "yes" if g.is_bipartite() else "no"
        #print(g)
        print("Case #%d: %s" % (i + 1, sol))
