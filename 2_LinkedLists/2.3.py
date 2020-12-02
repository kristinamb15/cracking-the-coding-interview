# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (any node but the first and last),
# given only access to that node
# Ex: delete c from a, b, c, d, e, f

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1:
# O(N) or less, really whatever it takes to get to the element
def delete_mid(llist, data):
    current = llist.head.next
    while current.next is not None:
        if current.data == data:
            current.data = current.next.data
            current.next = current.next.next
            break
        current = current.next
    return llist

# Solution 2: without invoking the list at all
# O(1)
def delete_mid_alt(el):
    if el is None or el.next is None:
        return False
    else:
        el.data = el.next.data
        el.next = el.next.next

# Testing
class Tests(unittest.TestCase):

    def test_delete_mid_single_occur(self):
        llist = SLinkedList()
        llist.add_multi(1, 5, 9, 12)
        self.assertEqual(delete_mid(llist, 9).data_list(), [1,5,12])

    def test_delete_mid_multi_occur(self):
        llist = SLinkedList()
        llist.add_multi(1, 3, 4, 5, 6, 8, 3, 4)
        self.assertEqual(delete_mid(llist, 4).data_list(), [1,3,5,6,8,3,4])
    
    def test_delete_mid_false(self):
        llist = SLinkedList()
        llist.add_multi(1, 2)
        self.assertEqual(delete_mid(llist, 3).data_list(), [1,2])
    
    def test_delete_mid_alt(self):
        node1 = Node(1)
        node5 = Node(5)
        node9 = Node(9)
        node12 = Node(12)
        node1.next = node5
        node5.next = node9
        node9.next = node12
        llist = SLinkedList(node1)
        delete_mid_alt(node9)
        self.assertEqual(llist.data_list(), [1,5,12])

if __name__ == '__main__':
    unittest.main()