import sys

N, M = map(int, input().split())
friend = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    friend[a].append(b)
    friend[b].append(a)
for i in range(N):
    friend[i] = list(set(friend[i]))
kb = [len(friend[i]) for i in range(N + 1)]

for i in range(1, N + 1):
    p = friend[i].copy()
    level = 2
    while True:
        d = len(p)
        for j in range(d):
            for k in friend[p[j]]:
                if k not in p and k != i:
                    p.append(k)
        t = len(p) - d
        kb[i] += t * level
        level += 1
        if t == 0:
            break

print(kb.index(min(kb[1:])))
