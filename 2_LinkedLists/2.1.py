# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# Follow up: How would you solve this problem if a temporary buffer is not allowed?

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1:
# O(N)
def remove_dups(llist):
    current = llist.head
    already = {current.data}
    while current.next is not None:
        if current.next.data not in already:
            already.add(current.next.data)
        else:
            current.next = current.next.next
        current = current.next
    return llist

# Solution 2:
# O(N^2)
def remove_dups_alt(llist):
    current = llist.head
    while current is not None:    
        compare_prev = current
        compare = current.next    
        while compare is not None:
            if current.data == compare.data:
                compare_prev.next = compare.next
                compare = compare.next
            else:
                compare_prev = compare
                compare = compare.next
        current = current.next
    return llist
    
# Solution 3: Ideal - modified solution 2, since the compare-prev isn't needed if we just use compare as a runner and look at its next element
# O(N^2)
def remove_dups_ideal(llist):
    current = llist.head
    while current is not None:    
        runner = current    
        while runner.next is not None:
            if current.data == runner.next.data:
                runner.next = runner.next.next  
            else:              
                runner = runner.next
        current = current.next
    return llist

# Testing
class Tests(unittest.TestCase):
    
    def test_remove_dups(self):
        llist = SLinkedList()
        llist.add_multi(2, 1, 3, 2, 4)
        self.assertEqual(remove_dups(llist).data_list(), [2,1,3,4])
    
    def test_remove_dups_alt(self):
        llist = SLinkedList()
        llist.add_multi(1, 3, 5, 3, 2, 4)
        self.assertEqual(remove_dups_alt(llist).data_list(), [1,3,5,2,4])
    
    def test_remove_dups_ideal(self):
        llist = SLinkedList()
        llist.add_multi(1, 2, 3, 4, 5, 3, 2)
        self.assertEqual(remove_dups_ideal(llist).data_list(), [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()
