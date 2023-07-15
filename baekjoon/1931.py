import sys

N = int(input())
t = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().strip().split())
    t.append((s, e))
t.sort(key=lambda x: (x[1], x[0]))
n = t[0][1]
res = [t[0]]
for i, j in enumerate(t):
    if n <= j[1] and n <= j[0] and i != 0:
        res.append(j)
        n = j[1]
print(len(res))
