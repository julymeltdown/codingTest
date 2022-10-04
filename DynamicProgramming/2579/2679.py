import sys

N = int(sys.stdin.readline())
stairs = [0]
dp = [0] * (N + 1)

for i in range(N):
    stairs.append(int(sys.stdin.readline()))
dp[1] = stairs[1]
if N == 1:
    print(dp[1])
    exit(0)
dp[2] = stairs[1] + stairs[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

print(dp[-1])
