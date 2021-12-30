import sys
MAX = 10000
a = [True] * MAX
a[0] = False
a[1] = False
i = 2
while i <= MAX // 2:
    j = 2
    while i * j < MAX:
        a[i * j] = False
        j += 1
    i += 1
t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    low = n // 2
    high = n // 2
    while not (a[low] and a[high]):
        low -= 1
        high += 1
    print(str(low) + ' ' + str(high))
