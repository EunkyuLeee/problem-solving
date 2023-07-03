import sys


class LinkedList:
    class Node:
        def __init__(self, d):
            self.data = d
            self.prev = None
            self.next = None

        def setLink(self, p, n):
            self.prev = p
            self.next = n

        def setPrev(self, p):
            self.prev = p

        def setNext(self, n):
            self.next = n

    def __init__(self):
        self.head = self.Node(0)
        self.tail = self.Node(0)
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head)
        self.cursor = self.tail

    def addChar(self, c):
        t = self.Node(c)
        t.setLink(self.cursor.prev, self.cursor)
        self.cursor.prev.setNext(t)
        self.cursor.setPrev(t)

    def moveCursor(self, right=False):
        if right:
            if self.cursor != self.tail:
                self.cursor = self.cursor.next
        else:
            if self.cursor != self.head.next:
                self.cursor = self.cursor.prev

    def delChar(self):
        if self.cursor != self.head.next:
            t = self.cursor.prev
            self.cursor.setPrev(t.prev)
            t.prev.setNext(self.cursor)
            del t

    def print(self):
        t = self.head.next
        while t != self.tail:
            print(t.data, end='')
            t = t.next


a = input()
myList = LinkedList()
for i in a:
    myList.addChar(i)
n = int(input())
for i in range(n):
    o = sys.stdin.readline()
    if o[0] == 'L':
        myList.moveCursor()
    elif o[0] == 'D':
        myList.moveCursor(right=True)
    elif o[0] == 'B':
        myList.delChar()
    elif o[0] == 'P':
        myList.addChar(o[2])
myList.print()
