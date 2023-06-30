def fact(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(fact(b) // (fact(a) * fact(b - a)))
