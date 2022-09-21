import sys

N = int(sys.stdin.readline())

cards = dict()

for _ in range(N):
    card = int(sys.stdin.readline().rstrip())

    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

answer = sorted(list(cards.items()), key=lambda x: (-x[1], x[0]))

print(answer[0][0])
