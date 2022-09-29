N = list(map(int, input()))
N.sort(reverse=True)

if 0 not in N:
    print(-1)
else:
    if sum(N) % 3 != 0:
        print(-1)
    else:
        print("".join(list(map(str, N))))
