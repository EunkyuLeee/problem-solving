class Stack:
    def __init__(self):
        self.data = [0 for i in range(1000)]
        self.size = 0

    def push(self, d):
        self.data[self.size] = d
        self.size += 1

    def pop(self):
        self.size -= 1
        if self.size >= 0:
            return self.data[self.size]
        else:
            return -1

    def isEmpty(self):
        return self.size == 0


left = ['(', '[', '{']
right = [')', ']', '}']

while True:
    isBalance = True
    stack = Stack()
    n = input()
    if n == ".":
        break
    for i in n:
        if i in left:
            stack.push(left.index(i))
        if i in right:
            tmp = stack.pop()
            if tmp != right.index(i) or tmp == -1:
                isBalance = False
                break
    if isBalance and stack.isEmpty():
        print("yes")
    else:
        print("no")
