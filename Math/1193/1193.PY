X = int(input())

line = 0
counter = 0
for i in range(0, X + 1):
    if line + i < X:
        line = line + i
    else:
        counter = i
        break

arr1 = [i for i in range(counter, 0, -1)]
arr2 = [i + 1 for i in range(counter)]

if counter % 2 == 0:
    print(str(arr2[X - line - 1]) + "/" + str(arr1[X - line - 1]))
else:
    print(str(arr1[X - line - 1]) + "/" + str(arr2[X - line - 1]))
