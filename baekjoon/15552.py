import sys

t = int(input())
for i in range(t):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    print(a+b)
