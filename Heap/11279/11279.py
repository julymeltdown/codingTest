import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num > 0:
        heappush(heap, -num)
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            pop = -heappop(heap)
            print(pop)
