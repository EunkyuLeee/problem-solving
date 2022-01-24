import sys

k = int(input())
arr = []
index = 0
for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        arr.pop(index-1)
        index -= 1
    else:
        arr.append(n)
        index += 1
print(sum(arr))
