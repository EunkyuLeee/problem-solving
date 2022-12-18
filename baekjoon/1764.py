n, m = map(int, input().split())

d = {}
l = []
for i in range(n):
    d[input()] = 1
for i in range(m):
    tmp = input()
    if tmp in d.keys():
        l.append(tmp)

print(len(l))
l.sort()
for i in l:
    print(i)
