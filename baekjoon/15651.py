from itertools import product

n, m = input().split()
n = int(n)
m = int(m)
a = list(product(range(1, n+1), repeat=m))
for i in a:
    for j in i:
        print(j, end=' ')
    print()
