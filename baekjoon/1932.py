import sys

n = int(input())
current = [0]
for i in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    cost[0] += current[0]
    for j in range(1, i):
        cost[j] += max(current[j-1], current[j])
    cost[i] += current[i-1]
    current = cost[:]
print(max(current))
