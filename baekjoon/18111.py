import sys

n, m, b = map(int, sys.stdin.readline().split())
land = [[] for i in range(n)]
minTime = sys.maxsize
landHeight = 0

for i in range(n):
    land[i] = list(map(int, sys.stdin.readline().split()))
for i in range(257):
    count = 0
    block = b
    for j in range(n):
        for k in range(m):
            l = land[j][k]
            temp = l - i
            count += 2 * temp if l > i else -temp
            block += temp
    if count <= minTime and block >= 0:
        landHeight = i
        minTime = count

print(minTime, landHeight)
