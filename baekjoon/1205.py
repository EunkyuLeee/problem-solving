n, score, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

num = 0
rank = 1
rankList = list(map(int, input().split()))

for i in rankList:
    if score <= i:
        num += 1
        if score < i:
            rank += 1

if num >= p:
    print(-1)
else:
    print(rank)
