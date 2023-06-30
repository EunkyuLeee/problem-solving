n = int(input())
paper = [[0 for i in range(100)] for j in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    for a in range(10):
        for b in range(10):
            paper[y + a][x + b] = 1

count = 0

for a in range(100):
    for b in range(100):
        if paper[a][b] == 1:
            count += 1

print(count)