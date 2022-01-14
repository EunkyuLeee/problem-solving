import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
d = {}
for i in a:
    d[i] = True
m = int(input())
b = list(map(int, sys.stdin.readline().split()))
for i in b:
    if i in d:
        print(1, end=' ')
    else:
        print(0, end=' ')
