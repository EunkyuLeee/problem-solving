import copy
import sys

n, m = input().split()
n = int(n)
m = int(m)
data = [['' for i in range(m)] for j in range(n)]
for j in range(n):
    data[j] = list(map(str, sys.stdin.readline()))
for j in range(n):
    data[j].remove('\n')


def check(i, j):
    temp = 0
    for b in range(j, j + 7):
        if board[i][b] == board[i][b + 1]:
            if board[i][b] == 'W':
                board[i][b + 1] = 'B'
            else:
                board[i][b + 1] = 'W'
            temp += 1
    for a in range(i + 1, i + 8):
        for b in range(j, j + 8):
            if board[a][b] == board[a - 1][b]:
                if board[a - 1][b] == 'W':
                    board[a][b] = 'B'
                else:
                    board[a][b] = 'W'
                temp += 1
    return temp


Min = n * m

for i in range(n - 7):
    for j in range(m - 7):
        board = copy.deepcopy(data)
        t = check(i, j)
        if t < Min:
            Min = t
for i in range(n - 7):
    for j in range(m - 7):
        board = copy.deepcopy(data)
        if board[i][j] == 'B':
            board[i][j] = 'W'
        else:
            board[i][j] = 'B'
        t = check(i, j) + 1
        if t < Min:
            Min = t

print(Min)
