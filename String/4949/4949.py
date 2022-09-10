from collections import deque

while True:
    sentence = list(input())
    if sentence == ["."]:
        break

    # 맨 마지막 . 삭제
    sentence = sentence[:len(sentence) - 1]
    answer = "yes"
    bracketArr = deque()
    wordArr = deque()

    for i in sentence:
        if i == "(" or i == "[":
            bracketArr.append(i)

        elif i == ")" or i == "]":
            if len(bracketArr) > 0:
                popped = bracketArr.pop()
            else:
                answer = "no"
                break

            if i == ")" and popped == "(":
                continue
            elif i == "]" and popped == "[":
                continue
            else:
                answer = "no"
                break
        else:
            wordArr.append(i)
    if len(bracketArr) > 0:
        answer = "no"
    print(answer)
