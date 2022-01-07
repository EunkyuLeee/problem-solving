import itertools
import sys

n = int(input())
s = []
per = []
for i in range(n):
    per.append(i+1)
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    s.append(temp)
com = itertools.combinations(per, n // 2)
mini = 0
for index, combi in enumerate(com):
    permu = itertools.permutations(combi, 2)
    start = 0
    for i in permu:
        start += s[i[0]-1][i[1]-1]
    link_per = per[:]
    for i in combi:
        link_per.remove(i)
    permu = itertools.permutations(link_per, 2)
    link = 0
    for i in permu:
        link += s[i[0]-1][i[1]-1]
    if index == 0:
        mini = abs(start - link)
    else:
        if mini > abs(start - link):
            mini = abs(start - link)
print(mini)
