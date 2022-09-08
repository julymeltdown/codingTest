arr = [0, 1, 1]


def fiboFunc(N):
    length = len(arr)
    if num >= length:
        for i in range(length, N + 1):
            arr.append(arr[i - 1] + arr[i - 2])


num = int(input())

fiboFunc(num)
print(arr[num])
