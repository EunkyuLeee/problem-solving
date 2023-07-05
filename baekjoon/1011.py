import sys

t = int(input())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    dis = y - x
    k = int((y - x) ** (1/2))
    res = 0
    if k ** 2 == dis:
        res = k * 2 - 1
    elif k ** 2 < dis <= k * (k + 1):
        res = k * 2
    elif k * (k + 1) < dis < (k + 1) ** 2:
        res = k * 2 + 1
    print(res)
