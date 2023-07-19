import sys

N, M = map(int, input().split())
maze = []
searched = [(0, 0)]
for i in range(N):
    tmp = list(int(i) for i in sys.stdin.readline().strip())
    maze.append(tmp)
idx = 0
count = 1
maze[0][0] = 0
while True:
    d = len(searched)
    while idx < d:
        if searched[idx] == (N - 1, M - 1):
            print(count)
            exit()
        a, b = searched[idx][0], searched[idx][1]
        if a > 0:
            if maze[a - 1][b] == 1:
                maze[a - 1][b] = 0
                searched.append((a - 1, b))
        if a < N - 1:
            if maze[a + 1][b] == 1:
                maze[a + 1][b] = 0
                searched.append((a + 1, b))
        if b > 0:
            if maze[a][b - 1] == 1:
                maze[a][b - 1] = 0
                searched.append((a, b - 1))
        if b < M - 1:
            if maze[a][b + 1] == 1:
                maze[a][b + 1] = 0
                searched.append((a, b + 1))
        idx += 1
    count += 1
