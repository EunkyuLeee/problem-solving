import sys

t = int(input())
num = [0 for i in range(101)]
for i in range(3):
    num[i] = 1
num[3] = 2
num[4] = 2
for i in range(5, 101):
    num[i] = num[i-1] + num[i-5]
for i in range(t):
    n = sys.stdin.readline()
    n = int(n)
    print(num[n-1])
