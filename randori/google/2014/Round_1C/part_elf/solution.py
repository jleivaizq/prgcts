import sys
from fractions import gcd


if __name__ == '__main__':

    cases = int(sys.stdin.readline())

    for case in range(cases):

        a, b = map(int, sys.stdin.readline().split('/'))

        g = gcd(a, b)
        a //= g
        b //= g

        # If b is not power of 2, then impossible
        if b & (b - 1):
            print("Case #%d: %s" % (case + 1, 'impossible'))
        else:
            t = 0
            while a < b:
                a *= 2
                t += 1
            print("Case #%d: %d" % (case + 1, t))


