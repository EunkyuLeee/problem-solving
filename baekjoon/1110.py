n = int(input())
i = 0
b = n
while True:
    i += 1
    a = int(b / 10) + (b % 10)
    b = (b % 10) * 10 + (a % 10)
    if b == n:
        print(i)
        break
