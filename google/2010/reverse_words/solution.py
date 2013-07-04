import sys

def reverse(lst):
    if len(lst) <= 0:
        return []
    else:
        head = lst.pop()
        return [head] + reverse(lst)

if __name__ == '__main__':
    cases = int(sys.stdin.readline())
    for i in xrange(cases):
        words = map(str, sys.stdin.readline().split())
        print("Case #%d: %s" % (i + 1, " ".join(reverse(words))))