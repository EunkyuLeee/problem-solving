N, K = map(int, input().split())
t = [-1 for _ in range(200001)]
q = [N]
t[N] = 0
for i in q:
    if i < 0 or 100000 < i:
        continue
    if i > 0:
        if t[i - 1] == -1:
            t[i - 1] = t[i] + 1
            q.append(i - 1)
    if t[i + 1] == -1:
        t[i + 1] = t[i] + 1
        q.append(i + 1)
    if t[i * 2] == -1:
        t[i * 2] = t[i] + 1
        q.append(i * 2)
    if i - 1 == K:
        print(t[i - 1])
        break
    elif i + 1 == K:
        print(t[i + 1])
        break
    elif i * 2 == K:
        print(t[i * 2])
        break
