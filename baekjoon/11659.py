import sys

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
s = 0
for i in nums:
    s += i
    sums.append(s)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    ret = sums[j] - sums[i - 1]
    print(ret)
