import sys

N = int(sys.stdin.readline())

books = dict()

for _ in range(N):
    book = sys.stdin.readline().rstrip()

    if books.get(book) is None:
        books[book] = 1
    else:
        books[book] += 1

answer = sorted(list(books.items()), key=lambda x: (-x[1],x[0]))

print(answer[0][0])
