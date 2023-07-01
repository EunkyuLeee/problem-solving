n = int(input())
a = list(map(int, input().split()))
p = [0 for i in range(n)]

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            p[i] += 1
        elif a[i] == a[j] and i > j:
            p[i] += 1

for i in p:
    print(i, end=' ')
