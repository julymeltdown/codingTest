import sys

N = int(input())

employee = dict()

for _ in range(N):
    name, status = sys.stdin.readline().split()
    employee[name] = status

for i in sorted(list(employee.items()), reverse=True):
    if i[1] == "enter":
        print(i[0])
