# 3.3 Stack of Plates: Imagine a literal stack of plates. If the stack gets too high, it might topple.
# In real life, we would start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. It should be composed of seversal stacks and should create a new stack once the previous one exceeds capacity.
# push and pop should behave identically to a single stack.
# Follow up: Implement a function popAt(index) which performs a pop on a specific substack.

class SetOfStacks:
    def __init__(self, cap = 10):
        self.cap = cap
        self.values = [[]]
        self.sizes = [0]
        self.main = 0
    
    def newStack(self):
        self.values.append([])
        self.sizes.append(0)
    
    def setPush(self, item):
        if self.sizes[self.main] == self.cap:
            self.newStack()
            self.main += 1
        
        self.values[self.main].append(item)
        self.sizes[self.main] += 1
    
    def setPop(self):
        item = self.values[self.main].pop()
        self.sizes[self.main] -= 1
        
        if self.sizes[self.main] == 0:
            self.values.pop()
            self.sizes.pop()
            self.main -= 1
        
        return item
    
    def pushMulti(self, *args):
        for x in args:
            self.setPush(x)
    
    # Solution if we don't rollover the bottom element of the next stack to keep previous stacks at cap
    def popAt(self, index):
        if index == self.main:
            item = self.setPop()
        else:
            item = self.values[index].pop()
            self.sizes[index] -= 1
            if self.sizes[index] == 0:
                self.values.pop(index)
                self.sizes.pop(index)
                self.main -= 1
    
    # Solution if we do rollover the bottom element of the next stack to keep previous stacks at cap
    def popAtRoll(self, index):
        self.popAt(index)
        if index != self.main:
            rollover = self.values[index + 1].pop(0)
            self.values[index].append(rollover)
            self.sizes[index] += 1
            self.sizes[index + 1] -= 1

    

ex1 = SetOfStacks(3)
ex1.pushMulti(1, 2, 3, 4, 5, 6, 7, 8)
print(ex1.values)
print(ex1.sizes)
ex1.popAtRoll(1)
print(ex1.values)
print(ex1.sizes)