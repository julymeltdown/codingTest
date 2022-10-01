import math

N = list(input())

d = dict()

for i in N:
    if i == "6" or i == "9":
        d["6,9"] = math.ceil((N.count("6") + N.count("9"))/2)
    else:
        d[i] = N.count(i)

answer = sorted(list(d.items()), key=lambda x: -x[1])
print(answer[0][1])