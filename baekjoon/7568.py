import sys

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in a:
    rank = 1
    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
