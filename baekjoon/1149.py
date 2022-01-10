import sys

n = int(input())
other_index = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
current = [0, 0, 0]
for i in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    for j in range(3):
        cost[j] += min(current[other_index[j][0]], current[other_index[j][1]])
    current = cost[:]
print(min(current))
