def isHansoo(a):
    digit = [a % 10000 // 1000, a % 1000 // 100, a % 100 // 10, a % 10]
    if digit[0] == 0:
        del digit[0]
        if digit[0] == 0:
            del digit[0]
            if digit[0] == 0:
                del digit[0]
    i = 1
    length = len(digit)
    while i < length and 1 < length:
        dif = digit[0] - digit[1]
        if digit[i-1] - digit[i] != dif:
            break
        i += 1
    if i == length or length == 1 or length == 2:
        return True
    else:
        return False


a = int(input())
count = 0
for j in range(1, a+1):
    if isHansoo(j):
        count += 1
print(count)