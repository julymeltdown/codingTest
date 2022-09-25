from collections import deque

N, M, K = map(int, input().split())
graph = [[0 for i in range(M)] for i in range(N)]

trashes = deque()

for _ in range(K):
    x, y = map(int, input().split())
    trashes.append((x - 1, y - 1))

    graph[x - 1][y - 1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while trashes:
    x, y = trashes.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or N <= nx or M <= ny:
            continue
        if graph[nx][ny] > 0:
            graph[nx][ny] = graph[x][y] + 1

maxNum = 0
for i in graph:
    maxNum = max(maxNum, max(i))

print(maxNum)
