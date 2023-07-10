N = int(input())
M = int(input())
bList = []

opm = N - 100 if N > 100 else 100 - N
if M != 0:
    bList = list(input().split())
elif M == 10:
    print(opm)
    exit()
else:
    t = len(list(str(N)))
    print(t if t < opm else opm)
    exit()

b = 0
d = 0
while d < opm:
    isValid = True
    n1 = list(str(N - d))
    for i in n1:
        if i in bList:
            isValid = False
            break
    if isValid and N >= d:
        b = len(n1) + d
        break
    isValid = True
    n2 = list(str(N + d))
    for i in n2:
        if i in bList:
            isValid = False
            break
    if isValid:
        b = len(n2) + d
        break
    d += 1

print(opm if opm < b or b == 0 else b)
