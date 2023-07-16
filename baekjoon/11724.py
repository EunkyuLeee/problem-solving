import sys

N, M = map(int, input().split())
link = [[] for _ in range(N + 1)]
search = []
for i in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    if u not in search:
        search.append(u)
    if v not in search:
        search.append(v)
    link[u].append(v)
    link[v].append(u)
count = 0
for i in search:
    tmp = []
    for j in link[i]:
        tmp.append(j)
    for j in tmp:
        for k in link[j]:
            if k not in tmp:
                tmp.append(k)
    for j in tmp:
        search.remove(j)
    count += 1
for i, j in enumerate(link):
    if len(j) == 0 and i != 0:
        count += 1
print(count)
