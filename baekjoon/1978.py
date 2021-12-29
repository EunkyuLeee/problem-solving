n = int(input())
a = list(map(int, input().split()))
numPrime = 0
for i in a:
    j = 2
    if i == 1:
        continue
    while j <= i // 2 + 1:
        if i % j == 0:
            break
        j += 1
    if j > i // 2:
        numPrime += 1
print(numPrime)
