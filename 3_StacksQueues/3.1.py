# 3.1 Three in One: Describe how you could use a single array to implement three stacks.

import unittest

class MultiStack:
    def __init__(self, stack_quantity, max_size = None):
        self.stack_quantity = stack_quantity
        self.max_size = max_size
        self.values = [[] for i in range(self.stack_quantity)]
        self.sizes = [0 for i in range(self.stack_quantity)]
    
    def isFull(self, stack_no):
        return self.sizes[stack_no] == self.max_size
    
    def isEmpty(self, stack_no):
        return self.sizes[stack_no] == 0
    
    def addItem(self, stack_no, item):
        if self.isFull(stack_no):
            raise Exception("Stack is full")
        else:
            self.values[stack_no].append(item)
            self.sizes[stack_no] += 1
    
    def addMulti(self, stack_no, *args):
        for x in args:
            if self.isFull(stack_no):
                stack_no += 1
            self.addItem(stack_no, x)
    
    def popItem(self, stack_no):
        if self.isEmpty(stack_no):
            raise Exception("Stack is empty")
        else:
            self.sizes[stack_no] -= 1
            return self.values[stack_no].pop()
    
    def peekTop(self, stack_no):
        if self.isEmpty(stack_no):
            raise Exception("Stack is empty")
        else:
            return self.values[stack_no][-1]
    
    def printStacks(self):
        for i in range(self.stack_quantity):
            if self.isEmpty(i):
                print(f"Stack {i}: empty")
            else:
                print(f"Stack {i}: {self.values[i]}")

# Testing
class Tests(unittest.TestCase):
    def setUp(self):
        self.stacks =  MultiStack(3, 3)
        self.stacks.addMulti(0, 1, 2, 3, 4)

    def test_multi_stack_values(self):
        self.assertEqual(self.stacks.values, [[1,2,3], [4], []])
    
    def test_multi_stack_sizes(self):
        self.assertEqual(self.stacks.sizes, [3,1,0])
    
    def test_multi_stack_isFull_true(self):
        self.assertTrue(self.stacks.isFull(0))

    def test_multi_stack_isFull_false(self):
        self.assertFalse(self.stacks.isFull(1))
    
    def test_multi_stack_isEmpty_true(self):
        self.assertTrue(self.stacks.isEmpty(2))

    def test_multi_stack_isEmpty_false(self):
        self.assertFalse(self.stacks.isEmpty(1))
    
    def test_multi_stack_peekTop(self):
        self.assertEqual(self.stacks.peekTop(0), 3)

    def test_multi_stack_peekTop_err(self):
        self.assertRaises(Exception, self.stacks.peekTop, 2)
    
    def test_multi_stack_popItem(self):
        self.assertEqual(self.stacks.popItem(1), 4)
    
    def test_multi_stack_popItem_err(self):
        self.assertRaises(Exception, self.stacks.popItem, 2)

if __name__ == '__main__':
    unittest.main()