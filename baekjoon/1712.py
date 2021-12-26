import sys

a, b, c = sys.stdin.readline().split()
a = int(a)
b = int(b)
c = int(c)
if b > c:
    print(-1)
elif b == c:
    if a == 0:
        print(1)
    else:
        print(-1)
else:
    print(a // (c - b) + 1)