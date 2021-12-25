num = [0 for i in range(9)]
word = str(input())
for i in word:
    if (ord(i) - 65) // 3 < 5:
        num[((ord(i) - 65) // 3)+1] += 1
    else:
        if 80 <= ord(i) <= 83:
            num[6] += 1
        elif 84 <= ord(i) <= 86:
            num[7] += 1
        elif 87 <= ord(i) <= 90:
            num[8] += 1
time = 0
for i in range(9):
    if num[i] != 0:
        time += (2 + i) * num[i]
print(time)