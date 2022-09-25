#https://www.acmicpc.net/board/view/69802 반례

from collections import deque

N, M, K = map(int, input().split())
graph = [[0 for i in range(M)] for i in range(N)]

coordinateQueue = deque()

for _ in range(K):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph
    coordinateQueue.append((x - 1, y - 1))

passQueue = deque()


def bfs(graph, ix, iy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((ix, iy))
    graph[ix][iy] = 0
    counter = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 1:
                if (nx, ny) in coordinateQueue:
                    passQueue.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1
                counter += 1
                queue.append((nx, ny))
    return counter


answer = []

for x, y in coordinateQueue:
    if (x, y) in passQueue:
        continue
    counter = bfs(graph, x, y)
    answer.append(counter)
print(graph)
print(max(answer))

