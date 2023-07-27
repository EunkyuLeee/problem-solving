import sys


def D(num):
    return (num * 2) % 10000


def S(num):
    return num - 1 if num != 0 else 9999


def L(num):
    if num >= 1000:
        return ((num % 1000) * 10) + (num // 1000)
    else:
        return num * 10


def R(num):
    return (num // 10) + ((num % 10) * 1000)


T = int(input())
s = ['D', 'S', 'L', 'R']
for _ in range(T):
    n = ['' for _ in range(10000)]
    src, dest = map(int, sys.stdin.readline().strip().split())
    searched = [src]
    idx = 0
    tmp = []
    while dest not in tmp:
        tmp = [D(searched[idx]), S(searched[idx]), L(searched[idx]), R(searched[idx])]
        for i, j in enumerate(tmp):
            if n[j] == '' and j != src:
                searched.append(j)
                n[j] = n[searched[idx]] + s[i]
        idx += 1
    print(n[dest])
