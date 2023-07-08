import sys

N, M = map(int, input().split())
d = {}
for i in range(N):
    t = sys.stdin.readline().strip().split()
    d[t[0]] = t[1]
for j in range(M):
    print(d[sys.stdin.readline().strip()])
