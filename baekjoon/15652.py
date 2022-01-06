from itertools import combinations_with_replacement

n, m = input().split()
n = int(n)
m = int(m)
a = list(combinations_with_replacement(range(1, n+1), m))
isPrint = 1
for i in a:
    for j in i:
        print(j, end=' ')
    print()
