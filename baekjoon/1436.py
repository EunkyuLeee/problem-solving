n = int(input())
num = 0
i = 0
while True:
    if num == n:
        break
    i += 1
    temp = i
    digit = []
    while temp > 0:
        digit.insert(0, temp % 10)
        temp = temp // 10
    for j in range(len(digit) - 2):
        if digit[j] == digit[j+1] == digit[j+2] == 6:
            num += 1
            break
print(i)
