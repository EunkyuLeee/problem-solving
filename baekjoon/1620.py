n, m = map(int, input().split())

d1 = {}
d2 = {}
idx = 1
for i in range(n):
    tmp = input()
    d1[idx] = tmp
    d2[tmp] = idx
    idx += 1

for j in range(m):
    tmp = input()
    if tmp.isdigit():
        print(d1[int(tmp)])
    else:
        print(d2[tmp])
