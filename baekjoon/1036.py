import sys

N = int(input())
strList = []
numList = [0 for i in range(36)]
d = {}
for i in range(36):
    if i < 10:
        d[str(i)] = i
    else:
        d[chr(ord('A') + i - 10)] = i
for i in range(N):
    strList.append(sys.stdin.readline().strip())
    for idx, j in enumerate(reversed(strList[i])):
        numList[d[j]] += (35 - d[j]) * (36 ** idx)
K = int(input())
cList = []
for i in range(K):
    cList.append(numList.index(max(numList)))
    numList[numList.index(max(numList))] = 0
total = 0
for i in strList:
    s = 0
    for idx, j in enumerate(reversed(i)):
        if d[j] in cList:
            s += 35 * (36 ** idx)
        else:
            s += d[j] * (36 ** idx)
    total += s
m = []
while total >= 36:
    m.append(total % 36)
    total //= 36
res = [str(total) if 0 <= total <= 9 else chr(ord('A') + total - 10)]
for a in reversed(m):
    res.append(str(a) if 0 <= a <= 9 else chr(ord('A') + a - 10))
for i in res:
    print(i, end='')
