import sys

T = int(input())
for i in range(T):
    n = int(sys.stdin.readline().strip())
    d = {}
    res = 1
    for j in range(n):
        name, kind = sys.stdin.readline().strip().split()
        if kind not in d.keys():
            d[kind] = 2
        else:
            d[kind] += 1
    for k in d.values():
        res *= k
    print(res - 1)
