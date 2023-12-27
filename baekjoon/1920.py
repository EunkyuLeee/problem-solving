import sys


def binSearch(num, arr, s, e):
    mid = (s + e) // 2
    if s == e:
        return 1 if arr[mid] == num else 0
    elif num < arr[mid]:
        return binSearch(num, arr, s, mid)
    elif num > arr[mid]:
        return binSearch(num, arr, mid + 1, e)
    else:
        return 1


n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in b:
    print(binSearch(i, a, 0, n - 1))
