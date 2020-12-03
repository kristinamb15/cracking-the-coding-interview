# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

import unittest

from linked_list import (Node, SLinkedList)

def reverse_list(llist):
    curr = llist.head
    rev_list=SLinkedList()

    while curr is not None:
        new = Node(curr.data)
        new.next = rev_list.head
        rev_list.head = new
        curr = curr.next

    return rev_list

# Solution 1:
# O(N)
def palindrome(llist):
    curr1 = llist.head
    rev_llist = reverse_list(llist)
    curr2 = rev_llist.head

    while curr1 is not None:
        if curr1.data != curr2.data:
            result = False
            break
        else:
            result = True
        curr1 = curr1.next
        curr2 = curr2.next
    
    return result

# Testing
class Tests(unittest.TestCase):

    def test_palindrome_false(self):
        llist = SLinkedList()
        llist.add_multi(1, 2, 3, 4, 5)
        self.assertFalse(palindrome(llist))
    
    def test_palindrome_true(self):
        llist = SLinkedList()
        llist.add_multi(1, 2, 3, 2, 1)
        self.assertTrue(palindrome(llist))

if __name__ == '__main__':
    unittest.main()