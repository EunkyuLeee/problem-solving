N = int(input())
P = list(map(int, input().split()))
P.sort()
s = 0
for i, v in enumerate(reversed(P)):
    s += v * (i + 1)
print(s)
