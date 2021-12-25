word = input()
num = [0 for i in range(26)]
for i in word:
    if 65 <= ord(i) <= 90:
        num[ord(i) - 65] += 1
    elif 97 <= ord(i) <= 122:
        num[ord(i) - 97] += 1
maxValue = max(num)
if num.count(maxValue) != 1:
    print("?")
else:
    maxIndex = num.index(maxValue)
    print(chr(maxIndex + 65))