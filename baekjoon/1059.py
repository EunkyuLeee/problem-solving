l = int(input())
s = list(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
else:
    s.sort()
    a = 0
    b = 0
    count = 0
    for i in s:
        if i < n:
            a = i
        if i > n and b == 0:
            b = i
    for i in range(a + 1, n + 1):
        for j in range(n, b):
            count += 1
    print(count - 1)
