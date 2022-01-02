import sys

n = int(input())
a = [0] * 10001
for i in range(n):
    a[int(sys.stdin.readline())] += 1
for i in range(len(a)):
    if a[i] != 0:
        for j in range(a[i]):
            sys.stdout.write(str(i) + '\n')
