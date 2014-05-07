import sys
import math

GRAVITY = 9.8

def work_out_angle(D, V):
    return 0.5*math.degrees(math.asin(round(D*GRAVITY/V**2, 9)))


if __name__ == '__main__':
    cases = int(sys.stdin.readline())
    for i in xrange(cases):
        velocity, distance = (float(x) for x in sys.stdin.readline().split())
        #print("Input #%d: D=%d, V=%.4f" % (i + 1, distance, velocity))
        print("Case #%d: %.7f" % (i + 1, work_out_angle(distance, velocity)))
