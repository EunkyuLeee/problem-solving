maxIndex = 0
maxVal = 0
for i in range(9):
    a = int(input())
    if maxVal < a:
        maxVal = a
        maxIndex = i+1
print(maxVal)
print(maxIndex)