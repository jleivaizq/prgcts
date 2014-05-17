import sys
from collections import defaultdict

def get_neighbors(b,i,j): 
    neighbors = []
    if i < nrows-1:
        neighbors.append((i+1,j))
    if i > 0:
        neighbors.append((i-1,j))
    if j < ncols-1:
        neighbors.append((i,j+1))
    if j > 0:
        neighbors.append((i,j-1))
    neighbors = [(ni,nj) for (ni,nj) in neighbors if b[ni][nj]>0]
    return neighbors 

def has_neighbors(b,i,j):
    return len(get_neighbors(b,i,j)) > 0

if __name__ == '__main__':

    cases = int(sys.stdin.readline())

    for num_case in range(cases):

        # Input
        nrows = int(sys.stdin.readline())
        ncols = int(sys.stdin.readline())

        board = []

        for j in range(nrows):
            board.append([int(x) for x in sys.stdin.readline().split()])

        # Play    
        turns = 0

        while(True):

            # Clean the board 
            children = 0
            for i in range(nrows):
                for j in range(ncols):
                    if board[i][j] < 12:
                        board[i][j] = 0
            
            for i in range(nrows):
                for j in range(ncols):
                    if board[i][j] > 0:
                        if not has_neighbors(board,i,j):
                            board[i][j] = 0
                        else:
                            children += 1

            # Check for end-state
            if not children:
                sol = '{} turns'.format(turns)
                break

            # Work out delta
            delta = defaultdict(int)
            for i in range(nrows):
                for j in range(ncols):
                    if board[i][j] > 0:
                        delta[i,j] -= 12
                        neighbors = get_neighbors(board,i,j)
                        value = 12/len(neighbors)
                        for ni,nj in neighbors:
                            delta[ni, nj] += value

            # If delta has not children with negative marbles it goes forever
            if all(x >= 0 for x in delta.values()):
                sol = '{} children will play forever'.format(children)
                break

            # How many turns can we apply at one time
            k = 1 + min(((board[i][j] - 12) // -delta[i,j] 
                         for i in range(nrows)
                         for j in range(ncols)
                         if delta[i,j] < 0))
            
            # Run next k turns
            for i in range(nrows):
                for j in range(ncols):
                    board[i][j] = board[i][j] + k*delta[i,j]

            turns += k

        # Output
        print('Case #%d: %s' % (num_case + 1, sol))
