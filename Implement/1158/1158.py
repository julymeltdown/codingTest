N, K = map(int, input().split())

# 1부터 N까지 배열을 생성
arr = [i + 1 for i in range(N)]
answer = []
# 제거될 사람의 인덱스
current = 0
while arr:
    current += K - 1

    if current >= len(arr):
        current = current % len(arr)

    answer.append(str(arr.pop(current)))
print("<", end="")
print(*answer, sep=", ", end="")
print(">")
