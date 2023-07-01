class PlanetarySystem:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isInclude(self, x, y):
        xDis = x - self.x if x > self.x else self.x - x
        yDis = y - self.y if y > self.y else self.y - y
        pDis = (xDis ** 2 + yDis ** 2) ** (1/2)
        return pDis < self.r


t = int(input())

for i in range(t):
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    pList = []
    count = 0
    for j in range(n):
        px, py, pr = map(int, input().split())
        pList.append(PlanetarySystem(px, py, pr))
        if pList[j].isInclude(sx, sy) ^ pList[j].isInclude(ex, ey):
            count += 1
    print(count)
