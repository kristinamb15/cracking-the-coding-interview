# 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop, and min should all operate in O(1) time.

import unittest
from queue import LifoQueue

# Solution 1:
# O(N)?
def stackMin(stack):
    stack_min = stack.get()
    while stack.qsize() != 0:
        new = stack.get()
        if new < stack_min:
            stack_min = new
    print(str(stack_min))
    return stack_min

ex1 = LifoQueue()
ex1.put(1)
ex1.put(2)
ex1.put(3)
stackMin(ex1)

# Note: I need to implement my own class to really answer this question
# Soluton 2:
# O(1)
class lifoStack:
    def __init__(self):
        self.values = []
        self.minList = []
    
    def stackMin(self):
        if len(self.minList) == 0:
            return None
        else:
            return self.minList[-1]
    
    def pushStack(self, item):
        if self.stackMin() is None:
            self.minList.append(item)
        elif item < self.stackMin():
            self.minList.append(item)              
        self.values.append(item)
    
    def pushMulti(self, *args):
        for x in args:
            self.pushStack(x)
    
    def popStack(self):
        item = self.values.pop()
        if item == self.stackMin():
            self.minList.pop()
        return item

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.lstack = lifoStack()
        self.lstack.pushMulti(5, 2, 3, 4, 1)

    def test_stackMin(self):
        self.assertEqual(self.lstack.stackMin(), 1)
    
    def test_stackMin_after_pop(self):
        self.lstack.popStack()
        self.assertEqual(self.lstack.stackMin(), 2)

if __name__ == '__main__':
    unittest.main()