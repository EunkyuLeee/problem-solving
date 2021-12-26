n = int(input())
i = 1
temp = 1
n -= 1
if n == 0:
    print(1)
else:
    while n >= temp:
        temp += 6 * i
        i += 1

    print(i)