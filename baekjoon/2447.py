paint = [[' ' for i in range(3 ** 8)] for j in range(3 ** 8)]
loc = [0, 0]
n = int(input())


def star(a, x, y):
    if a == 3:
        for i in range(3):
            paint[x][y] = '*'
            x += 1
        x -= 3
        y += 1
        paint[x][y] = '*'
        x += 2
        paint[x][y] = '*'
        x -= 2
        y += 1
        for i in range(3):
            paint[x][y] = '*'
            x += 1
        return
    else:
        x1 = x
        y1 = y
        for i in range(3):
            star(a // 3, x1, y1)
            x1 += a // 3
        x1 -= a
        y1 += a // 3
        star(a // 3, x1, y1)
        x1 += a // 3 * 2
        star(a // 3, x1, y1)
        x1 -= a - a // 3
        y1 += a // 3
        for i in range(3):
            star(a // 3, x1, y1)
            x1 += a // 3


star(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(paint[i][j], end='')
    print()
