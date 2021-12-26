x = int(input())
i = 1
a = 1
b = 1
Sum = 2
isChanged = 0
while i < x:
    if (a == 1 or b == 1) and isChanged == 0:
        Sum += 1
        if a > b:
            a += 1
        else:
            b += 1
        isChanged = 1
    else:
        if Sum % 2 == 1:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
        isChanged = 0
    i += 1

print(str(a) + '/' + str(b))
