import sys

def solve(cards):

    result = 0

    finished = len(cards) <= 1

    while not finished:
        i = 1
        while (i < len(cards)):
            if cards[i] < cards[i-1]:
                moving_card = cards[i]
                result = result + 1
                j = 0
                while j < i and moving_card > cards[j]: j = j+1
                aux = cards[j]
                cards.remove(moving_card)
                cards.insert(cards.index(aux), moving_card)
            i = i + 1
        if i >= len(cards)-1:
            finished = True

    return result

if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in range(cases):
        number_cards = int(sys.stdin.readline())
        cards = []
        for nc in range(number_cards):
            cards.append(sys.stdin.readline())
        sol = solve(cards)
        print("Case #%d: %d" % (i + 1, sol))


