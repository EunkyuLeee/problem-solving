import sys
from operator import itemgetter

n = int(input())
a = []
for i in range(n):
    temp = list(map(str, sys.stdin.readline().split()))
    temp[0] = int(temp[0])
    a.append(temp)
a.sort(key=itemgetter(0))
for i in a:
    print(str(i[0]) + ' ' + str(i[1]))
