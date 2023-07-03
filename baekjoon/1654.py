k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))
lan.sort()
l, h = 1, max(lan)
res = 0
while l <= h:
    s = 0
    m = (l + h) // 2
    for i in lan:
        s += i // m
    if s < n:
        h = m - 1
    else:
        if res < m:
            res = m
        l = m + 1

print(res)
