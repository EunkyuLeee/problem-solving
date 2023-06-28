import sys

p = int(input())

for i in range(p):
    s = list(map(int, sys.stdin.readline().split()))
    t = s[0]
    s.remove(t)
    total = 0
    for j, stu in enumerate(s):
        count = 0
        for k in range(j):
            if s[k] > stu:
                count += 1
        total += count
    print(t, total)
