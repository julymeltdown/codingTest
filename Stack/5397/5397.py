import sys

# 테스트케이스 개수
T = int(input())

for _ in range(T):
    sentence = list(sys.stdin.readline().rstrip())
    left = []
    right = []
    for i in range(len(sentence)):
        if sentence[i] == "<":
            if len(left) > 0:
                right.append(left.pop())
        elif sentence[i] == ">":
            if len(right) > 0:
                left.append(right.pop())
        elif sentence[i] == "-":
            if len(left) > 0:
                left.pop()
        else:
            left.append(sentence[i])

    left = left + list(reversed(right))
    print("".join(left))
