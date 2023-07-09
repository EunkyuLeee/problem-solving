N, r, c = map(int, input().split())
res = 0
n = 2 ** N
while n > 1:
    n //= 2
    if r < n and c < n:
        res += 0
    elif r < n <= c:
        res += n ** 2
    elif c < n <= r:
        res += (n ** 2) * 2
    else:
        res += (n ** 2) * 3
    if n <= c:
        c -= n
    if n <= r:
        r -= n

print(res)