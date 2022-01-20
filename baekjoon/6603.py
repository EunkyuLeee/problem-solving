import itertools
import sys

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s.pop(0)
    if k == 0:
        break
    com = itertools.combinations(s, 6)
    for i in com:
        for j in i:
            print(j, end=' ')
        print()
    print()