X = int(input())
length = 64
count = 0

while X > 0:
    if length > X:
        length = length / 2
    else:
        count += 1
        X -= length

print(count)
