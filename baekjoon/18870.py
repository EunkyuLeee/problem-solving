import sys

n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
a = list(set(temp[:]))
a.sort()
dict_a = {}
for i, e in enumerate(a):
    dict_a[e] = i
for i in range(n):
    sys.stdout.write(str(dict_a[temp[i]]) + ' ')
