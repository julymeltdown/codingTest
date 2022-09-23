import sys

tempSum = 0

for _ in range(10):

    num = int(sys.stdin.readline())

    if abs(100 - (tempSum + num)) <= abs(100 - tempSum):
        tempSum = tempSum + num
    else:
        break

print(tempSum)
