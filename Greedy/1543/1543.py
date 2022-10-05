word = list(input())
sample = list(input())
sampleLen = len(sample)

counter = 0
answer = 0
while True:
    if word[counter:counter + sampleLen] == sample:
        counter += sampleLen
        answer += 1
    else:
        counter += 1

    if counter == len(word):
        break

print(answer)
