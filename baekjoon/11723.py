import sys

m = int(input())

s = [0 for i in range(20)]

for i in range(m):
    o = sys.stdin.readline().split()
    c = o[0]

    if c == "all":
        for j in range(20):
            s[j] = 1
        continue
    elif c == "empty":
        for j in range(20):
            s[j] = 0
        continue

    n = int(o[1]) - 1

    if c == "add":
        s[n] = 1
    elif c == "remove":
        s[n] = 0
    elif c == "check":
        print(s[n])
    elif c == "toggle":
        s[n] = 1 - s[n]
