import sys
from operator import itemgetter

n = int(input())
a = [list(map(int, sys.stdin.readline().split()))]
for i in range(n - 1):
    a.append(list(map(int, sys.stdin.readline().split())))
a = sorted(a, key=itemgetter(1))
a = sorted(a, key=itemgetter(0))

for i in a:
    sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')
