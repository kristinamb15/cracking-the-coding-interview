# 3.1 Three in One: Describe how you could use a single array to implement three stacks.

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
            self.addItem(stack_no, x)
            self.sizes[stack_no] += 1
    
    def popItem(self, stack_no):
        if self.isEmpty(stack_no):
            raise Exception("Stack is empty")
        else:
            self.sizes[stack_no] -= 1
            self.values[stack_no].pop()
    
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


stacks = MultiStack(3, 3)
stacks.addMulti(0, 1, 2, 3)
stacks.printStacks()