n = int(input())
bList = list(map(int, input().split()))

maxB = 0
for i, b in enumerate(bList):
    isFirst = True
    d = 0
    numB = 0
    for j in range(i):
        tmp = (bList[i - j - 1] - bList[i]) / (j + 1)
        if isFirst or tmp > d:
            isFirst = False
            d = tmp
            numB += 1
        else:
            continue
    d = 0
    isFirst = True
    for j in range(len(bList) - i - 1):
        tmp = (bList[i + j + 1] - bList[i]) / (j + 1)
        if isFirst or tmp > d:
            isFirst = False
            d = tmp
            numB += 1
        else:
            continue
    if maxB < numB:
        maxB = numB
print(maxB)
