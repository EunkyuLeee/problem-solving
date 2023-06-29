n = int(input())

pan = [['_' for i in range(n)] for j in range(n)]

hi = 0
hj = 0

head = 0
lArm = 0
rArm = 0
back = 0
lLeg = 0
rLeg = 0

isRight = False

for i in range(n):
    pan[i] = input()
    for j, c in enumerate(pan[i]):
        if 0 < j < n-1 and 0 < i < n-1:
            if c == '*' and pan[i][j-1] == '*' and pan[i][j+1] == '*' and pan[i-1][j] == '*':
                hi = i
                hj = j
                x = 0
                y = 0
                while hi - y >= 0:
                    if pan[hi - y][hj] == '*':
                        head += 1
                    y += 1
                for k, t in enumerate(pan[i]):
                    if t == '*' and not isRight:
                        lArm = hj - k
                        isRight = True
                    elif isRight and t == '_':
                        rArm = k - hj - 1
                        isRight = False
                if rArm == 0:
                    rArm = n - hj - 1
                continue
        if hi != 0 and hj != 0 and c == '*':
            if j == hj:
                back += 1
            elif j == hj - 1:
                lLeg += 1
            elif j == hj + 1 and i != hi:
                rLeg += 1

print(hi + 1, hj + 1)
print(lArm, rArm, back, lLeg, rLeg)
