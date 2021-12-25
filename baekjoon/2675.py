import sys

t = int(input())
for i in range(t):
    a, b = sys.stdin.readline().split()
    a = int(a)
    temp = ''
    for j in b:
        for k in range(a):
            temp += j
    print(temp)