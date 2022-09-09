T = int(input())
counter = 0

for _ in range(T):
    word = list(input())
    characters = []
    isGroupWord = True
    for i in range(len(word)):
        if word[i] not in characters:
            characters.append(word[i])

        else:
            if word[i] != word[i - 1]:
                isGroupWord = False
                break

    if isGroupWord:
        counter += 1

print(counter)
