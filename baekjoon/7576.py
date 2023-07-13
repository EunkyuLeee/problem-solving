import sys

M, N = map(int, input().split())
t = []
n = []
s = []
e = 0
count = 0
for i in range(N):
    t.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(N):
    for j in range(M):
        if t[i][j] == 1:
            s.append((i, j))
        elif t[i][j] == -1:
            e += 1
idx = 0
isEnd = True
while idx < M * N - e:
    if not isEnd:
        print(-1)
        exit()
    d = len(s)
    isEnd = False
    while idx < d:
        a, b = s[idx][0], s[idx][1]
        if a - 1 >= 0:
            if t[a - 1][b] == 0:
                t[a - 1][b] = 1
                s.append((a - 1, b))
                isEnd = True
        if a + 1 < N:
            if t[a + 1][b] == 0:
                t[a + 1][b] = 1
                s.append((a + 1, b))
                isEnd = True
        if b - 1 >= 0:
            if t[a][b - 1] == 0:
                t[a][b - 1] = 1
                s.append((a, b - 1))
                isEnd = True
        if b + 1 < M:
            if t[a][b + 1] == 0:
                t[a][b + 1] = 1
                s.append((a, b + 1))
                isEnd = True
        idx += 1
    count += 1
print(count - 1)
