import itertools
import operator


def div(a, b):
    if b < 0 <= a or a <= 0 < b:
        return -(abs(a) // abs(b))
    else:
        return a // b


ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": div
}

n = int(input())
num = list(map(int, input().split()))
opr = list(map(int, input().split()))
operate = []
for index, value in enumerate(opr):
    if index == 0 and value != 0:
        for i in range(value):
            operate.append("+")
    elif index == 1 and value != 0:
        for i in range(value):
            operate.append("-")
    elif index == 2 and value != 0:
        for i in range(value):
            operate.append("*")
    elif index == 3 and value != 0:
        for i in range(value):
            operate.append("/")
permute = itertools.permutations(operate)
maxi = 0
mini = 0
for j, i in enumerate(permute):
    temp = num[0]
    for index, value in enumerate(num):
        if index != 0:
            temp = ops[i[index-1]](temp, value)
    if j == 0:
        maxi = temp
        mini = temp
    else:
        if maxi < temp:
            maxi = temp
        if mini > temp:
            mini = temp
print(maxi)
print(mini)
