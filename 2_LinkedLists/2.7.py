# 2.7 Intersection: Given two singly linked lists, determine if the two lists intersect. Return the intersecting node.

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1: Note that this solution isn't really correct - it compares the lists to see if they are the same from a certain point, but we need lists that have the same references
# O(NM)
def intersect(llist1, llist2):
    if llist1.length() > llist2.length():
        [longer, shorter] = [llist1, llist2]
    else:
        [longer, shorter] = [llist2, llist1]
    
    cur1 = longer.head
    result = False

    while cur1 is not None:
        cur2 = shorter.head
        if cur1.data == cur2.data:
            intersect_node = cur1
            while cur1.next is not None:
                if cur1.next.data == cur2.next.data:
                    result = True
                else:
                    result = False
                cur1 = cur1.next
                cur2 = cur2.next
        else:
            cur1 = cur1.next
    
    if result:
        return (result,intersect_node.data)
    else:
        return result

# Solution 2
def list_intersect(llist1, llist2):
    if llist1.length() > llist2.length():
        [longer, shorter] = [llist1, llist2]
    else:
        [longer, shorter] = [llist2, llist1]
    
    cur1 = longer.head
    result = False

    while cur1 is not None:
        cur2 = shorter.head
        if cur1 == cur2:
            intersect_node = cur1
            while cur1.next is not None:
                if cur1.next == cur2.next:
                    result = True
                else:
                    result = False
                cur1 = cur1.next
                cur2 = cur2.next
        else:
            cur1 = cur1.next
    
    if result:
        return (result,intersect_node.data)
    else:
        return result

# Testing
class Tests(unittest.TestCase):
    
    def test_intersect_true(self):
        llist1 = SLinkedList()
        llist1.add_multi(1, 2, 3, 4, 5)
        llist2 = SLinkedList()
        llist2.add_multi(2, 3, 4, 5) 

        self.assertEqual(intersect(llist1, llist2), (True,2))
    
    def test_intersect_false(self):
        llist1 = SLinkedList()
        llist1.add_multi(1, 2, 3, 4, 5)
        llist2 = SLinkedList()
        llist2.add_multi(6, 7, 7, 8) 

        self.assertFalse(intersect(llist1, llist2))

    def test_list_intersect_true(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        llist1 = SLinkedList(node1)
        llist2 = SLinkedList(node2)

        self.assertEqual(list_intersect(llist1, llist2), (True,2))
        
if __name__ == '__main__':
    unittest.main()