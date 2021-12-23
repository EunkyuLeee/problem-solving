n, x = input().split()
n = int(n)
x = int(x)
a = list(map(int, input().split()))
for i in a:
    if i < x:
        print(i, end=' ')
