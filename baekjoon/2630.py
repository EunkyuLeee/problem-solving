N = int(input())
w, b = 0, 0
P = []
for i in range(N):
    P.append(list(map(int, input().split())))


def check(x, y, s):
    global w, b, P
    if s == 1:
        if P[y][x] == 0:
            w += 1
        else:
            b += 1
        return
    isOne = True
    prev = P[y][x]
    i = 0
    while i < s:
        j = 0
        while j < s:
            if P[y + i][x + j] != prev:
                isOne = False
                break
            j += 1
        i += 1
    if isOne:
        if P[y][x] == 0:
            w += 1
        else:
            b += 1
    else:
        check(x, y, s // 2)
        check(x + (s // 2), y, s // 2)
        check(x, y + (s // 2), s // 2)
        check(x + (s // 2), y + (s // 2), s // 2)


check(0, 0, N)
print(w)
print(b)
