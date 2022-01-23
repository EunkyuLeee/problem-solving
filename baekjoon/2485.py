import math
import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
dis = []
temp = 0
arr.sort()
for i in range(len(arr) - 1):
    dis.append(arr[i+1] - arr[i])
    if i == 0:
        temp = arr[i+1] - arr[i]
    else:
        temp = math.gcd(temp, arr[i+1] - arr[i])
count = 0
for i in range(1, len(arr)):
    count += (arr[i] - arr[i-1]) // temp - 1
print(count)
