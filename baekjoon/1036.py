import itertools
import sys


def strto36(s):
    res = 0
    for k in reversed(range(len(s))):
        if ord('0') <= ord(s[len(s) - k - 1]) <= ord('9'):
            res += int(s[len(s) - k - 1]) * (36 ** k)
        else:
            res += (10 + ord(s[len(s) - k - 1]) - ord('A')) * (36 ** k)
    return res


def i36tos(num):
    m = []
    while num > 36:
        m.append(num % 36)
        num //= 36
    resStr = [str(num) if 0 <= num <= 9 else chr(ord('A') + num - 10)]
    for a in reversed(m):
        resStr.append(str(a) if 0 <= a <= 9 else chr(ord('A') + a - 10))
    return resStr


input = sys.stdin.readline
N = int(input())
strList = []
nums = [i for i in range(36)]
total = 0
S = set()
for i in range(N):
    t = input()
    strList.append(t)
    total += strto36(t)
    S.update(t)
K = int(input())
for i in list(itertools.combinations(S, K if K <= len(S) else len(S))):
    t_tot = 0
    subList = []
    for j in strList:
        tmp = list(j)
        for idx, p in enumerate(tmp):
            if p in i:
                tmp[idx] = 'Z'
        subList.append(tmp)
    for j in subList:
        t_tot += strto36(j)
    if t_tot > total:
        total = t_tot
for i in i36tos(total):
    print(i, end='')
