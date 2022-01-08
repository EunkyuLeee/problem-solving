import sys

a = [[] for i in range(41)]
a[0] = [1, 0]
a[1] = [0, 1]
for i in range(2, 41):
    a[i] = [j + k for j, k in zip(a[i-1], a[i-2])]
t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    print(a[n][0], a[n][1])
