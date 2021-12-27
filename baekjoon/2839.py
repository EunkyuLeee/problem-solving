n = int(input())
count = 0
temp = n
while temp > 0:
    temp -= 5
    count += 1
if temp == 0:
    print(count)
else:
    while True:
        temp += 5
        count -= 1
        if count < 0:
            print(-1)
            break
        elif (temp % 3) == 0:
            count += temp // 3
            print(count)
            break
