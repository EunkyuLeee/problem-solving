def num(a):
    if a == 1:
        return 1
    else:
        return num(a-1) * 2 + 1


def hanoi(a, start, end, via):
    if a == 1:
        print(start, end)
    else:
        hanoi(a - 1, start, via, end)
        print(start, end)
        hanoi(a - 1, via, end, start)


n = int(input())
print(num(n))
hanoi(n, 1, 3, 2)
