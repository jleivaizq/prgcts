import sys
import time
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)

PROBLEM = 'Reordering Train Cars'

def solve():
    return ''

if __name__ == '__main__':

    # Problem header
    logging.info('@ '+PROBLEM)
    global_time = time.time()

    # Number of cases
    cases = int(sys.stdin.readline())

    # Deal with each case
    for case in range(cases):
        case_time = time.time()
        sol = solve()
        print("Case #%d: %s" % (case + 1, sol))
        logging.info('@ Case {} time: '.format(time.time() - case_time))

    # Total time
    logging.info('@ Total time: {}'.format(time.time() - global_time))


