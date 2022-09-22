import sys

T = int(sys.stdin.readline())

for _ in range(T):
    closet = dict()
    clothesCount = int(sys.stdin.readline())
    for i in range(clothesCount):
        clothesName, body = sys.stdin.readline().split()
        if not closet.get(body):
            closet[body] = [clothesName]
        else:
            closet[body] = closet.get(body)+[clothesName]

    #print(closet)
    answer = 1
    for i in closet.values():
        answer = answer * (len(i)+1)

    print(answer-1)