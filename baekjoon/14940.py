import sys

n, m = map(int, input().split())
mapList = []
disList = []
searched = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    mapList.append(tmp)
    disList.append([0 for _ in tmp])
    try:
        searched.append((i, tmp.index(2)))
    finally:
        continue


def valid(a):
    ret = []
    if a[0] >= 1:
        ret.append((a[0] - 1, a[1]))
    if a[0] < n - 1:
        ret.append((a[0] + 1, a[1]))
    if a[1] >= 1:
        ret.append((a[0], a[1] - 1))
    if a[1] < m - 1:
        ret.append((a[0], a[1] + 1))
    return ret


count = 1
last = list(searched)
tmp = []
while True:
    for i in last:
        for y, x in valid(i):
            if mapList[y][x] == 1 and disList[y][x] == 0 and (y, x) != searched[0]:
                disList[y][x] = count
                searched.append((y, x))
                tmp.append((y, x))
        if i == last[-1]:
            last = list(tmp)
            tmp = []
            count += 1
    if len(last) == 0:
        break

for i in range(n):
    for j in range(m):
        if disList[i][j] == 0 and mapList[i][j] == 1 and (i, j) != searched[0]:
            disList[i][j] = -1
for i in range(n):
    for j in range(m):
        print(disList[i][j], end=' ')
    print()
