a, b = input().split()
minDiff = 51

for i in range(len(b) - len(a) + 1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            diff += 1
    if minDiff > diff:
        minDiff = diff

print(minDiff)