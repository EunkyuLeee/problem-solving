import sys

m, n = sys.stdin.readline().split()
m = int(m)
n = int(n)
a = [True] * (n+1)
i = 0
a[0] = False
a[1] = False
while i < m:
    a[i] = False
    i += 1
i = 2
while i < n:
    j = 2
    while i * j <= n:
        a[i * j] = False
        j += 1
    i += 1
for i in range(n + 1):
    if a[i]:
        print(i)
