n, k = input().split()
n = int(n)
k = int(k)
a = [i+1 for i in range(n)]
res = []
index = -1
for i in range(n):
    index += k
    if index >= len(a):
        index = index % len(a)
    res.append(a[index])
    a.remove(a[index])
    index -= 1
print("<", end='')
for i in range(n-1):
    print(res[i], end=', ')
print(str(res[n-1]) + '>')
