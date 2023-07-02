def fact(d):
    res = 1
    for i in range(1, d + 1):
        res *= i
    return res


n, k = map(int, input().split())
print(int(fact(n) / (fact(k) * fact(n - k))))
