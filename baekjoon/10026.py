import sys


def getNeighbor(p, n):
    ret = []
    if p[0] > 0:
        ret.append((p[0] - 1, p[1]))
    if p[0] < n - 1:
        ret.append((p[0] + 1, p[1]))
    if p[1] > 0:
        ret.append((p[0], p[1] - 1))
    if p[1] < n - 1:
        ret.append((p[0], p[1] + 1))
    return ret


N = int(input())
img = []
img2 = []
for i in range(N):
    img.append(list(sys.stdin.readline().strip()))
    img2.append(img[i].copy())
searched = [(0, 0)]
idx = 0
other = []
count = 1
t = img[searched[idx][0]][searched[idx][1]]
img[searched[idx][0]][searched[idx][1]] = ''
while idx < N * N:
    tmp = getNeighbor(searched[idx], N)
    for i in tmp:
        if img[i[0]][i[1]] == t:
            searched.append(i)
            img[i[0]][i[1]] = ''
        elif img[i[0]][i[1]] != '':
            other.append(i)
    idx += 1
    if idx == len(searched) and len(other) > 0:
        last = other.pop()
        while img[last[0]][last[1]] == '' and len(other) > 0:
            last = other.pop()
        if len(other) == 0:
            break
        searched.append(last)
        count += 1
        t = img[searched[idx][0]][searched[idx][1]]
        img[searched[idx][0]][searched[idx][1]] = ''
print(count, end=' ')

searched = [(0, 0)]
idx = 0
other = []
count = 1
t = img2[searched[idx][0]][searched[idx][1]]
img2[searched[idx][0]][searched[idx][1]] = ''
while idx < N * N:
    tmp = getNeighbor(searched[idx], N)
    for i in tmp:
        if img2[i[0]][i[1]] == t:
            searched.append(i)
            img2[i[0]][i[1]] = ''
        elif img2[i[0]][i[1]] != '':
            if ord(img2[i[0]][i[1]]) + ord(t) == ord('R') + ord('G'):
                searched.append(i)
                img2[i[0]][i[1]] = ''
            else:
                other.append(i)
    idx += 1
    if idx == len(searched) and len(other) > 0:
        last = other.pop()
        while img2[last[0]][last[1]] == '' and len(other) > 0:
            last = other.pop()
        if len(other) == 0:
            break
        searched.append(last)
        count += 1
        t = img2[searched[idx][0]][searched[idx][1]]
        img2[searched[idx][0]][searched[idx][1]] = ''
print(count)
