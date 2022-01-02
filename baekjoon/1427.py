n = int(input())
a = []
while n != 0:
    a.append(n % 10)
    n //= 10
a.sort(reverse=True)
for i in a:
    print(i, end='')