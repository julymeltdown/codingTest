from collections import deque

N = int(input())
temp = [i + 1 for i in range(N)]
cards = deque(temp)

answer = []
while cards:
    answer.append(cards.popleft())
    if cards:
        cards.append(cards.popleft())

print(" ".join(list(map(str, answer))))
