# 2.2 Return Kth to Last: implement an algorithm to find teh kth to last element of a singly linked list.

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1:
# O(N)
def kth_to_last(llist, k):
    current = llist.head
    llist_map = []
    while current is not None:
        llist_map.append(current.data)
        current = current.next

    kindex = len(llist_map) - k
    if kindex >= 0:
        kth = llist_map[kindex]
    else:
        kth = None
    return kth

# Testing
class Tests(unittest.TestCase):
    
    def test_kth_to_last_exists(self):
        llist = SLinkedList()
        llist.add_multi(1, 2, 3, 4, 5)
        self.assertEqual(kth_to_last(llist, 2), 4)
    
    def test_kth_to_last_not_exists(self):
        llist = SLinkedList()
        llist.add_multi(1, 2, 3)
        self.assertEqual(kth_to_last(llist, 4), None)

if __name__ == '__main__':
    unittest.main()