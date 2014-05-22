import sys
import time
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)

PROBLEM = 'Reordering Train Cars'

# XXX TODO: Take a look to: http://www.go-hero.net/jam/14/name/geohot

def is_valid(tcars):
    cars = set()
    #logging.info('Checking if {} is valid'.format(tcars))
    prev = None
    for tcar in tcars:
    #    logging.info('TC = {}'.format(tcar))
        for c in tcar:
    #        logging.info('Prev = {} Car = {} Set = {}'.format(prev, c, cars))
            if c != prev:
                if c not in cars:
                    cars.add(c)
                else:
                    return False
                prev = c
    return True

def valid_arrangements(tcars):
    head, *tail = tcars

    # base case
    if not tail:
        return [[head]]

    previous_arrangements = valid_arrangements(tail)

    result = []
    # logging.info(previous_arrangements)

    for arr in previous_arrangements:
        #logging.info('P.valid arr: {}'.format(arr))
        for pos in range(len(arr)+1):
        #    logging.info('({}) {} <-{}-> {}'.format(pos, arr[:pos], [head], arr[pos:]))
            arrangement = arr[:pos] + [head] + arr[pos:]
            if is_valid(arrangement):
        #        logging.info('{} is valid'.format(arrangement))
                result.append(arrangement)
        #    else:
        #        logging.info('{} is not valid'.format(arrangement))

    return result 
    
    

def solve():
    n = int(sys.stdin.readline())
    tcars = sys.stdin.readline().split()
    logging.info('@ Input {}'.format(tcars))
    sol = valid_arrangements(tcars)
    logging.info('@ Valid: {}'.format(sol))
    return len(sol)

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
        print("Case #%d: %s" % (case + 1, str(sol)))
        logging.info('@ Case {} time: {} ms'.format(case + 1, time.time() - case_time))

    # Total time
    logging.info('@ Total time: {} ms'.format(time.time() - global_time))


