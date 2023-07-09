import sys

T = int(input())
for i in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    b = []
    for j in range(K):
        X, Y = map(int, sys.stdin.readline().strip().split())
        b.append((X, Y))
    count = 0
    z = []
    while len(b) > 0:
        z.append(b[0])
        for j in z:
            if (j[0], j[1] - 1) in b and (j[0], j[1] - 1) not in z:
                z.append((j[0], j[1] - 1))
            if (j[0], j[1] + 1) in b and (j[0], j[1] + 1) not in z:
                z.append((j[0], j[1] + 1))
            if (j[0] - 1, j[1]) in b and (j[0] - 1, j[1]) not in z:
                z.append((j[0] - 1, j[1]))
            if (j[0] + 1, j[1]) in b and (j[0] + 1, j[1]) not in z:
                z.append((j[0] + 1, j[1]))
        count += 1
        for j in z:
            b.remove(j)
        z = []
    print(count)
