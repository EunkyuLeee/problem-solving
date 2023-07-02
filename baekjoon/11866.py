n, k = map(int, input().split())
p = [i + 1 for i in range(n)]
s = []
idx = -1
for i in range(n):
    count = 0
    while count < k:
        idx += 1
        idx %= n
        if p[idx] != 0:
            count += 1
    s.append(p[idx])
    p[idx] = 0
for i, j in enumerate(s):
    if i == 0:
        print("<", end='')
    print(j, end='')
    if i != len(s) - 1:
        print(",", end=' ')
    else:
        print(">", end='')
