n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort(reverse=True)
b.sort()
Sum = 0
for i in range(n):
    Sum += a[i] * b[i]
print(Sum)