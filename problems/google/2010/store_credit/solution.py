import sys

def solve(top_credit, items):

    solution = []

    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if items[i] + items[j] == top_credit:
                solution.append((i,j))

    return solution[0]


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        top_credit = int(sys.stdin.readline())
        number_items = int(sys.stdin.readline())
        items = map(int, sys.stdin.readline().split())
        (sol1, sol2) = solve(top_credit, items)
        print("Case #%d: %d %d" % (i + 1, sol1+1, sol2+1))

