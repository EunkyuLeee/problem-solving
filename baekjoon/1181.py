import sys

n = int(input())
a = []
for i in range(n):
    a.append(sys.stdin.readline())
a = set(a)
a = list(a)
a.sort()
a.sort(key=len)
for i in a:
    print(i, end='')
