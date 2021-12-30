import sys
while True:

    n = int(sys.stdin.readline())
    if n == 0:
        break
    a = [True] * (2 * n + 1)
    i = 0
    a[0] = False
    a[1] = False
    while i <= n:
        a[i] = False
        i += 1
    i = 2
    while i <= n:
        j = 2
        while i * j < 2 * n + 1:
            a[i * j] = False
            j += 1
        i += 1
    num = 0
    for i in range(n, 2 * n + 1):
        if a[i]:
            num += 1
    print(num)
