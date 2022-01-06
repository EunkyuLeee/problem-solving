from itertools import permutations

n, m = input().split()
n = int(n)
m = int(m)
a = list(permutations(range(1, n+1), m))
for i in a:
    for j in i:
        print(j, end=' ')
    print()
