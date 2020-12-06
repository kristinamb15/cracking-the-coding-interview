# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

import unittest
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
    
    def getQueue(self):
        queue_list = []
        while not self.queueStack.empty():
            temp = self.queueStack.get()
            queue_list.append(temp)
        return queue_list[::-1]
        while len(queue_list) > 0:
            temp = queue_list.pop()
            self.queueStack.put(temp)

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.myq = MyQueue()
        self.myq.pushMulti(1, 2, 3)

    def test_popQueue(self):
        self.assertEqual(self.myq.popQueue(), 1)
    
    def test_pushQueue(self):
        self.myq.pushQueue(0)
        self.assertEqual(self.myq.getQueue(), [0, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()