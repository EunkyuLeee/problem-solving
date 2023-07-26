import sys

M, N, H = map(int, input().split())
storage = [[] for __ in range(H)]
searched = []
empty = 0
for i in range(H):
    for j in range(N):
        t = list(map(int, sys.stdin.readline().strip().split()))
        storage[i].append(t)
        for k in range(M):
            if t[k] == 1:
                searched.append((i, j, k))
            elif t[k] == -1:
                empty += 1


def getNeighbor(a, b, c):
    ret = []
    if a > 0:
        ret.append((a - 1, b, c))
    if a < H - 1:
        ret.append((a + 1, b, c))
    if b > 0:
        ret.append((a, b - 1, c))
    if b < N - 1:
        ret.append((a, b + 1, c))
    if c > 0:
        ret.append((a, b, c - 1))
    if c < M - 1:
        ret.append((a, b, c + 1))
    return ret


d = len(searched)
idx = 0
count = -1
while d > 0:
    count += 1
    tmp = d
    d = 0
    for i in range(tmp):
        h, n, m = searched[idx + i]
        points = getNeighbor(h, n, m)
        for j in points:
            if storage[j[0]][j[1]][j[2]] == 0:
                storage[j[0]][j[1]][j[2]] = 1
                searched.append(j)
                d += 1
    idx += tmp
if len(searched) + empty < M * N * H:
    print(-1)
else:
    print(count)
