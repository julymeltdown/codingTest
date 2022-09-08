arr0=[0,1,1]
def fiboFunc(N):
    length=len(arr0)
    if num >= length:
        for i in range(length,N+1):
            arr0.append(arr0[i-1]+arr0[i-2])

num = int(input())
fiboFunc(num)
print(arr0[num])