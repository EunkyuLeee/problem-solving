n, m = input().split()
n = int(n)
m = int(m)
a = list(map(int, input().split()))
Max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if Max < a[i] + a[j] + a[k] <= m:
                Max = a[i] + a[j] + a[k]
print(Max)