import sys

N = int(input())
mapList = []
for i in range(N):
    tmp = sys.stdin.readline().strip()
    t = []
    for j in tmp:
        t.append(True if j == '1' else False)
    mapList.append(t)

countList = []
d = 0
while True:
    y, x = 0, 0
    isBreak = False
    for i in range(y, N):
        for j in range(x, N):
            if mapList[i][j]:
                y, x = i, j
                mapList[i][j] = False
                isBreak = True
                break
        if isBreak:
            break
    if not isBreak:
        break
    count = 1
    tmp = [(y, x)]
    for i in tmp:
        a, b = i[0], i[1]
        if a > 0:
            if mapList[a - 1][b]:
                mapList[a - 1][b] = False
                tmp.append((a - 1, b))
                count += 1
        if a < N - 1:
            if mapList[a + 1][b]:
                mapList[a + 1][b] = False
                tmp.append((a + 1, b))
                count += 1
        if b > 0:
            if mapList[a][b - 1]:
                mapList[a][b - 1] = False
                tmp.append((a, b - 1))
                count += 1
        if b < N - 1:
            if mapList[a][b + 1]:
                mapList[a][b + 1] = False
                tmp.append((a, b + 1))
                count += 1
    countList.append(count)
    d += 1
print(d)
for i in sorted(countList):
    print(i)
