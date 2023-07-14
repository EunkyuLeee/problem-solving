import sys


class MyHeap:
    def __init__(self):
        self.data = [0]

    def remove(self):
        if len(self.data) <= 1:
            return 0
        ret = self.data[1]
        if len(self.data) <= 2:
            ret = self.data.pop()
            return ret
        self.data[1] = self.data.pop()
        tmp = self.data[1]
        idx = 1
        while True:
            if idx * 2 + 1 < len(self.data):
                if tmp <= self.data[idx * 2] and tmp <= self.data[idx * 2 + 1]:
                    break
                if self.data[idx * 2] < self.data[idx * 2 + 1]:
                    t = self.data[idx * 2]
                    self.data[idx * 2] = tmp
                    self.data[idx] = t
                    idx = idx * 2
                else:
                    t = self.data[idx * 2 + 1]
                    self.data[idx * 2 + 1] = tmp
                    self.data[idx] = t
                    idx = idx * 2 + 1
            elif idx * 2 < len(self.data):
                if tmp <= self.data[idx * 2]:
                    break
                if tmp > self.data[idx * 2]:
                    t = self.data[idx * 2]
                    self.data[idx * 2] = tmp
                    self.data[idx] = t
                    idx = idx * 2
            else:
                break
        return ret

    def insert(self, n):
        self.data.append(n)
        idx = len(self.data) - 1
        while n < self.data[idx // 2] and idx > 1:
            tmp = self.data[idx // 2]
            self.data[idx] = tmp
            self.data[idx // 2] = n
            idx = idx // 2


N = int(input())
h = MyHeap()
for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        print(h.remove())
    else:
        h.insert(x)
