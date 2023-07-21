N, M = map(int, input().split())
tree = list(map(int, input().split()))
maxi = max(tree)
mini = 1
while maxi >= mini:
    d = (maxi + mini) // 2
    s = 0
    for j in tree:
        s += j - d if j > d else 0
    if s > M:
        mini = d + 1
    elif s < M:
        maxi = d - 1
    else:
        break
print((maxi + mini) // 2)
