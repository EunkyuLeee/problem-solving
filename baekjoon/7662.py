import sys


class MyMinHeap:
    def __init__(self):
        self.data = [0]

    def insert(self, num):
        self.data.append(num)
        d = len(self.data)
        if d == 2:
            return
        idx = d - 1
        while idx > 1 and self.data[idx] < self.data[idx // 2]:
            self.data[idx] = self.data[idx // 2]
            self.data[idx // 2] = num
            idx //= 2

    def remove(self):
        if len(self.data) == 1:
            return False
        ret = self.data[1]
        num = self.data.pop()
        if len(self.data) == 1:
            return ret
        idx = 1
        self.data[1] = num
        d = len(self.data)
        while idx * 2 + 1 < d:
            if self.data[idx * 2] < num or self.data[idx * 2 + 1] < num:
                if self.data[idx * 2] < self.data[idx * 2 + 1]:
                    self.data[idx] = self.data[idx * 2]
                    self.data[idx * 2] = num
                    idx = idx * 2
                else:
                    self.data[idx] = self.data[idx * 2 + 1]
                    self.data[idx * 2 + 1] = num
                    idx = idx * 2 + 1
            else:
                break
        while idx * 2 < d:
            if self.data[idx * 2] < num:
                self.data[idx] = self.data[idx * 2]
                self.data[idx * 2] = num
                idx = idx * 2
            else:
                break
        return ret


class MyMaxHeap:
    def __init__(self):
        self.data = [0]

    def insert(self, num):
        self.data.append(num)
        d = len(self.data)
        if d == 2:
            return
        idx = d - 1
        while idx > 1 and self.data[idx] > self.data[idx // 2]:
            self.data[idx] = self.data[idx // 2]
            self.data[idx // 2] = num
            idx //= 2

    def remove(self):
        if len(self.data) == 1:
            return False
        ret = self.data[1]
        num = self.data.pop()
        if len(self.data) == 1:
            return ret
        idx = 1
        self.data[1] = num
        d = len(self.data)
        while idx * 2 + 1 < d:
            if self.data[idx * 2] > num or self.data[idx * 2 + 1] > num:
                if self.data[idx * 2] > self.data[idx * 2 + 1]:
                    self.data[idx] = self.data[idx * 2]
                    self.data[idx * 2] = num
                    idx = idx * 2
                else:
                    self.data[idx] = self.data[idx * 2 + 1]
                    self.data[idx * 2 + 1] = num
                    idx = idx * 2 + 1
            else:
                break
        while idx * 2 < d:
            if self.data[idx * 2] > num:
                self.data[idx] = self.data[idx * 2]
                self.data[idx * 2] = num
                idx = idx * 2
            else:
                break
        return ret


T = int(input())
for _ in range(T):
    k = int(sys.stdin.readline())
    dic = {}
    minHeap = MyMinHeap()
    maxHeap = MyMaxHeap()
    for __ in range(k):
        s = sys.stdin.readline()
        n = int(s[1:])
        if s[0] == 'I':
            minHeap.insert(n)
            maxHeap.insert(n)
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1
        elif n == 1:
            while True:
                t = maxHeap.remove()
                if str(t) == "False":
                    break
                if dic[t] != 0:
                    dic[t] -= 1
                    break
        elif n == -1:
            while True:
                t = minHeap.remove()
                if str(t) == "False":
                    break
                if dic[t] != 0:
                    dic[t] -= 1
                    break
    while True:
        maxValue = maxHeap.remove()
        if str(maxValue) == "False":
            break
        elif dic[maxValue] != 0:
            break
    while True:
        minValue = minHeap.remove()
        if str(minValue) == "False":
            break
        elif dic[minValue] != 0:
            break
    if str(maxValue) == "False" or str(minValue) == "False":
        print("EMPTY")
    else:
        print(maxValue, minValue)
