n, m, t = map(int, input().split())
if t % min(n, m) == 0:
    print(t // min(n, m), 0)
else:
    cokeTime = t
    hamburger = 0
    for i in range(t // min(n, m)+1):
        temp = t - min(n, m) * i
        tempHamburger = i + temp // max(n, m)
        temp = temp % max(n, m)

        if temp <= cokeTime and tempHamburger >= hamburger:
            cokeTime = temp
            hamburger = tempHamburger

    print(hamburger, cokeTime)
