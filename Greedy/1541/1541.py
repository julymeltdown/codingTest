from collections import deque

inputList = list(input())
expression = deque()
num = 0
for i in inputList:
    if i != "+" and i != "-":
        num = num * 10 + int(i)
    else:
        expression.append(num)
        num = 0
        expression.append(i)

expression.append(num)

beforeMinus = 0
afterMinus = 0

for i in list(expression):
    if i == "-":
        break
    if i != "+":
        beforeMinus += i
    expression.popleft()

for i in list(expression):
    if i != "+" and i != "-":
        afterMinus += i

print(beforeMinus - afterMinus)
