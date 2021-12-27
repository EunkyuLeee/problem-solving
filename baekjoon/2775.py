import sys

t = int(input())
Sum = 0
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    a = [[0 for col in range(n+1)] for row in range(k+1)]
    if k == 0:
        print(n)
    else:
        for j in range(1, n+1):
            a[0][j-1] = j
        for j in range(1, k+1):
            for m in range(1, n+1):
                for p in range(m):
                    a[j][m-1] += a[j-1][p]

        print(a[k][n-1])