from collections import deque

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    graph = []
    islandQ = deque()

    for i in range(H):
        temp = list(map(int, input().split()))
        for j in range(W):
            if temp[j] == 1:
                islandQ.append([i, j])

        graph.append(temp)

    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    counter = 0
    # print(islandQ)
    while islandQ:
        x, y = islandQ.popleft()
        if graph[x][y] == 1:
            counter += 1
            graph[x][y] = 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                # counter += 1
                islandQ.appendleft([nx, ny])
        # print(*graph,sep="\n")
        # print("-----------------")

    print(counter)
