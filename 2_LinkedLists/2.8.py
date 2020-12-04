# 2.8 Loop Detection: Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists)

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1
# O(N) - where N is the length up to the loop
def find_loop(llist):
    curr = llist.head
    already = []
    while curr not in already and curr is not None:
        already.append(curr)
        curr = curr.next
    if curr is None:
        return None
    else:
        return curr.data

# Solution 2
# O(N) where N is length of loop ?

def find_loop_alt(llist):
    slow_runner = llist.head
    fast_runner = llist.head

    while (fast_runner is not None) and (fast_runner.next is not None):
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner == fast_runner:
            loop = True
            break
        else:
            loop = False
    
    if loop:    
        slow_runner = llist.head
        while slow_runner != fast_runner:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next
    
    if loop:
        return fast_runner.data
    else:
        return None

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.nodeA = Node("A")
        self.nodeB = Node("B")
        self.nodeC = Node("C")
        self.nodeD = Node("D")
        self.nodeE = Node("E")

        self.nodeA.next = self.nodeB
        self.nodeB.next = self.nodeC
        self.nodeC.next = self.nodeD
        self.nodeD.next = self.nodeE
        self.nodeE.next = self.nodeC

        self.llist1 = SLinkedList(self.nodeA)
        self.llist2 = SLinkedList()
        self.llist2.add_multi(1, 2, 3, 4, 5)

    def test_find_loop_yes(self):
        self.assertEqual(find_loop(self.llist1), 'C')
    
    def test_find_loop_no(self):
        self.assertEqual(find_loop(self.llist2), None)
    
    def test_find_loop_alt_yes(self):
        self.assertEqual(find_loop_alt(self.llist1), 'C')
    
    def test_find_loop_alt_no(self):
        self.assertEqual(find_loop_alt(self.llist2), None)

if __name__ == '__main__':
    unittest.main()
