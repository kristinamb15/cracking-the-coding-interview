# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit, stored in reverse order.
# Write a function that adds the two numbers and returns the sum as a linked list.
# You cannot just convert the linked list to an integer.
# Follow up: Suppose the digits are stored in forward order

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1:
# O(N)
def sum_lists(llist1, llist2):
    cur1 = llist1.head
    cur2 = llist2.head
    result = SLinkedList()
    over = 0
    while (cur1 is not None) or (cur2 is not None):
        if cur1 is None:
            cur1 = Node(0)
        if cur2 is None:
            cur2 = Node(0)
        sums = cur1.data + cur2.data + over
        if sums >= 10:
            sums = sums - 10
            over = 1
        else:
            over = 0
        result.add_node(sums)
        cur1 = cur1.next
        cur2 = cur2.next
    if over == 1:
        result.add_node(1)
    return result

# Solution 2: digits stored in forward order
# O(N) ?
def sum_lists_forward(llist1, llist2):
    extra = llist1.length() - llist2.length()
    if extra > 0:
        for i in range(extra):
            new = Node(0)
            new.next = llist2.head
            llist2.head = new
    if extra < 0:
        for i in range(abs(extra)):
            new = Node(0)
            new.next = llist1.head
            llist1.head = new
    
    cur1 = llist1.head
    cur2 = llist2.head
    
    extra = SLinkedList()
    result = SLinkedList()
    while cur1 is not None:
        sums = cur1.data + cur2.data
        if sums >= 10:
            extra.add_node(1)
            sums = sums - 10
        else:
            extra.add_node(0)
        result.add_node(sums)
        cur1 = cur1.next
        cur2 = cur2.next
    extra.add_node(0)

    if not check_zero(extra):
        return sum_lists_forward(extra, result)
    else:
        return result

def check_zero(llist):
    is_zero = True
    current = llist.head
    while current is not None:
        if current.data != 0:
            is_zero = False
            break
        current = current.next
    return is_zero

# Testing
class Tests(unittest.TestCase):
    
    def setUp(self):
        self.llistA = SLinkedList()
        self.llistA.add_multi(7, 1, 6, 1)
        self.llistB = SLinkedList()
        self.llistB.add_multi(5, 9, 2)
        self.llistC = SLinkedList()
        self.llistC.add_multi(5, 1, 8)
        self.llistD = SLinkedList()
        self.llistD.add_multi(5, 4, 3)

    def test_sum_lists_without_0(self):
        self.assertEqual(sum_lists(self.llistA, self.llistB).data_list(), [2,1,9,1])
    
    def test_sum_lists_with_0(self):
        self.assertEqual(sum_lists(self.llistC, self.llistD).data_list(), [0,6,1,1])
    
    def test_sum_lists_forward(self):
        result = sum_lists_forward(self.llistA, self.llistB)
        self.assertEqual(result.data_list(), [0,7,7,5,3])

if __name__ == '__main__':
    unittest.main()
