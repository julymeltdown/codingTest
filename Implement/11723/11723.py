import sys

M = int(input())
results = []

for _ in range(M):
    S = sys.stdin.readline().rstrip()
    if S == 'all':
        results = [i + 1 for i in range(20)]
    elif S == 'empty':
        results = []
    else:
        a, b = S.split()
        n = int(b)
        if a == 'add':
            if n not in results:
                results.append(n)
        elif a == 'remove':
            if n in results:
                results.remove(n)
        elif a == 'toggle':
            if n in results:
                results.remove(n)
            else:
                results.append(n)
        else:
            if n in results:
                sys.stdout.write(str(1)+"\n")
            else:
                sys.stdout.write(str(0)+"\n")
