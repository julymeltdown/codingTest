import sys

N = int(sys.stdin.readline())
TArr = [0]
PArr = [0]
for _ in range(N):
    T, P = map(int, sys.stdin.readline().split())
    TArr.append(T)
    PArr.append(P)

dp = [0] * 20

for i in range(1, N + 1):
    x = TArr[i] - 1  # x는 i일에 상담을 하면 P기간만큼 일을 해야하므로 i일 당일 하루 빼고 TArr[i]-1 만큼 더해야하니까 선언한 수
    dp[i] = max(dp[i], dp[i - 1])
    dp[i + x] = max(dp[i - 1] + PArr[i], dp[i + x])

print(dp[N])
