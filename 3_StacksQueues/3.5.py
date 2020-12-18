# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure.
# The stack supports push, pop, peek, and isEmpty.

import unittest
from queue import LifoQueue

# LifoQueue has no built in peek method
def peek_stack(stack):
    item = stack.get()
    stack.put(item)
    return item

# Solution 1:
# O(n^2) ?
def sort_stack(stack):
    temp_stack = LifoQueue()

    while not stack.empty():
        # get next element of stack
        temp = stack.get()

        # Push temp stack elements back into stack until we find the right place for the temp element
        while not temp_stack.empty() and peek_stack(temp_stack) > temp:
            stack.put(temp_stack.get())

        # Put temp element in temp stack
        temp_stack.put(temp)           

    # Put elements back in stack    
    while not temp_stack.empty():
        stack.put(temp_stack.get())    
    
    return stack

# Turns stack into list for testing/printing
def list_stack(stack):
    printer = []
    while not stack.empty():
        temp = stack.get()
        printer.append(temp)
    for item in printer[::-1]:
        stack.put(item)
    return printer[::-1]

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.my_stack = LifoQueue()
        self.my_stack.put(4)
        self.my_stack.put(1)
        self.my_stack.put(2)
        self.my_stack.put(5)
        self.my_stack.put(3)

    def test_sort_stack(self):
        self.assertEqual(list_stack(sort_stack(self.my_stack)), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()