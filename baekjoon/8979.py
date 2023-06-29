class Medal:
    def __init__(self, g, s, b):
        self.gold = g
        self.silver = s
        self.bronze = b

    def __gt__(self, operand):
        if self.gold > operand.gold:
            return True
        elif self.gold == operand.gold:
            if self.silver > operand.silver:
                return True
            elif self.silver == operand.silver:
                if self.bronze > operand.bronze:
                    return True
        return False


n, k = map(int, input().split())

mList = []

for i in range(n):
    m = list(map(int, input().split()))
    num = m[0]
    if k == num:
        find = Medal(m[1], m[2], m[3])
    mList.append(Medal(m[1], m[2], m[3]))

rank = 1

for i in mList:
    if i > find:
        rank += 1

print(rank)
