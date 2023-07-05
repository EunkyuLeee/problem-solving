n = int(input())
count = 0
d = [0 for i in range(n + 1)]
for i in range(n + 1):
    if i <= 1:
        d[i] = 0
        continue
    elif i <= 3:
        d[i] = 1
        continue
    if i % 2 == 0 and i % 3 == 0:
        d[i] = min(d[i // 2], d[i // 3], d[i - 1])
    elif i % 3 == 0:
        d[i] = min(d[i // 3], d[i - 1])
    elif i % 2 == 0:
        d[i] = min(d[i // 2], d[i - 1])
    else:
        d[i] = d[i - 1]
    d[i] += 1
print(d[n])
