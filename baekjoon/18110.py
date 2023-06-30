n = int(input())
lList = []
s = 0

for i in range(n):
    lList.append(int(input()))

lList.sort()

cut = n * 15 // 100
cut += 1 if n * 15 % 100 >= 50 else 0

for i in range(cut, n - cut):
    s += lList[i]

if n == 0:
    print(0)
else:
    level = s // len(range(cut, n - cut))
    level += 1 if s / len(range(cut, n - cut)) % 1 >= 0.5 else 0
    print(level)
