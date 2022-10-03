import sys

N = int(sys.stdin.readline())
numbers = [i + 1 for i in range(N)]
stack = []
pointer = 1
answer = []
for _ in range(N):
    num = int(sys.stdin.readline())
    while pointer <= num:
        stack.append(pointer)
        answer.append("+")
        pointer += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit(0)

print(*answer, sep="\n")
