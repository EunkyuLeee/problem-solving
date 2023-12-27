n, m = map(int, input().split())
edge = [[j for j in range(i + 1, i + 7)] for i in range(101)]
line = {}
for i in range(n + m):
    a, b = map(int, input().split())
    line[a] = b
dis = [999 for i in range(101)]
node = [1]
dis[1] = 0
if 1 in line.keys():
    dis[line[1]] = dis[1]
    node.append(line[1])
    node.remove(1)
while dis[100] == 999:
    tmp = node.copy()
    node = []
    for i in tmp:
        for j in edge[i]:
            if j > 100:
                continue
            if dis[j] > dis[i] + 1:
                dis[j] = dis[i] + 1
                node.append(j)
    tmp = node.copy()
    for i in tmp:
        if i in line.keys():
            dis[line[i]] = dis[i]
            node.append(line[i])
            node.remove(i)
print(dis[100])
