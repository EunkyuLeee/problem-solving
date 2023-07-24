import sys

T = int(input())
for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().strip().split())
    count = x
    isValid = False
    while x <= M * N and y <= M * N:
        if x == y:
            isValid = True
            break
        if x < y:
            x += M
        else:
            y += N
    if isValid:
        print(x)
    else:
        print(-1)
