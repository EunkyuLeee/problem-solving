import itertools
import sys

t = int(input())
arr = [1, 2, 3]
for i in range(t):
    n = int(sys.stdin.readline())
    count = 0
    for j in range(1, n+1):
        for k in itertools.product(arr, repeat=j):
            if sum(k) == n:
                count += 1
    print(count)
