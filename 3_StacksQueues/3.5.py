# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure.
# The stack supports push, pop. peed, and isEmpty.

from queue import LifoQueue

# Solution 1:
# O(n^2) ?
def sort_stack(stack):
    temp = LifoQueue()
    run = True
    while run:
        min_item = stack.get()
        while not stack.empty():
            next_item = stack.get()
            if min_item < next_item:
                temp.put(next_item)
            else:
                temp.put(min_item)
                min_item = next_item    
        
        temp_run = True
        while not temp.empty() and temp_run:
            # Would use peek here but it doesn't exist in LifoQueue
            item = temp.get()
            if item > min_item:
                stack.put(item)
            else:
                temp.put(item)
                temp_run = False
        
        temp.put(min_item)

        if stack.empty():
            run = False
    
    while not temp.empty():
        item = temp.get()
        stack.put(item)
    
    return stack

def printStack(stack):
    printer = []
    while not stack.empty():
        temp = stack.get()
        printer.append(temp)
    print(printer[::-1])
    while len(printer) > 0:
        temp = printer.pop()
        stack.put(temp)

ex1 = LifoQueue()
ex1.put(2)
ex1.put(1)
ex1.put(4)
ex1.put(3)
ex1.put(5)
printStack(ex1)

sort_stack(ex1)
printStack(ex1)