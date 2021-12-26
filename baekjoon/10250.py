import sys

t = int(input())
a = 0
b = 0
for i in range(t):
    h, w, n = sys.stdin.readline().split()
    h = int(h)
    w = int(w)
    n = int(n)
    a = n % h
    if a == 0:
        a = h
    b = (n - 1) // h + 1
    print(a * 100 + b)