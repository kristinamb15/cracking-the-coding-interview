# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

from queue import LifoQueue

class MyQueue:
    def __init__(self):
        self.tempStack = LifoQueue()
        self.queueStack = LifoQueue()

    def pushQueue(self, item):
        while not self.queueStack.empty():
            temp = self.queueStack.get()
            self.tempStack.put(temp)
        self.queueStack.put(item)
        while not self.tempStack.empty():
            temp = self.tempStack.get()
            self.queueStack.put(temp)
    
    def popQueue(self):
        return self.queueStack.get()
    
    def pushMulti(self, *args):
        for x in args:
            self.pushQueue(x)

    def printQueue(self):
        printer = []
        while not self.queueStack.empty():
            temp = self.queueStack.get()
            printer.append(temp)
        print(printer[::-1])
        while len(printer) > 0:
            temp = printer.pop()
            self.queueStack.put(temp)

ex1 = MyQueue()
ex1.pushMulti(1, 2, 3)
ex1.printQueue()
ex1.popQueue()
ex1.printQueue()
ex1.pushQueue(0)
ex1.printQueue()