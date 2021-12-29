m = int(input())
n = int(input())
Sum = 0
Min = n
for i in range(m, n+1):
    j = 2
    if i == 1:
        continue
    while j <= i // 2 + 1:
        if i % j == 0:
            break
        j += 1
    if j > i // 2:
        Sum += i
        if Min > i:
            Min = i
if Sum == 0:
    print(-1)
else:
    print(Sum)
    print(Min)