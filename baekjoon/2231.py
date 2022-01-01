n = int(input())
i = 0
isGen = 0
for i in range(n):
    temp = i
    a = []
    digit = 10
    while temp > 0:
        a.append(temp % 10)
        temp = (temp - temp % 10) // 10
    if i + sum(a) == n:
        isGen = 1
        break
if isGen:
    print(i)
else:
    print(0)