N, M = map(int, input().split())
dictionary = {}

for i in range(N):
    name = input()
    dictionary[name] = i + 1

dictValue = list(dictionary.keys())

for i in range(M):
    name = input()

    if name.isdigit():
        print(dictValue[int(name) - 1])
    else:
        find = dictionary.get(name)
        print(find)
