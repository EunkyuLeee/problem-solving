n = int(input())
t = int(input())

link = [[] for i in range(n + 1)]
infect = []
count = 0

for i in range(t):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for i in link[1]:
    infect.append(i)
    count += 1

index = 0

while index < len(infect):
    i = infect[index]
    for j in link[i]:
        if j not in infect and j != 1:
            infect.append(j)
            count += 1
    index += 1

print(count)
