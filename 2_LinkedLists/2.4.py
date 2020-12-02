# 2.4 Partition: Write code to partition a linked list around a value x, such that ll nodes less than x come before all nodes greater than or equal to x.
# The partition element x can be anywhere in the "right partition" - it doesn't have to be in the middle
# Ex: 3, 5, 8, 5, 10, 2, 1 becomes 3, 1, 2, 10, 5, 5, 8

import unittest

from linked_list import (Node, SLinkedList)

# Solution 1:
# O(N)
def partition(llist, value):
    head = llist.head
    part = Node("*")

    if head.data >= value:
        part.next = head
        llist.head = part
        head = llist.head
        runner_prev = part.next
    else:
        part.next = head.next
        head.next = part
        runner_prev = part

    while runner_prev.next is not None:
        runner = runner_prev.next
        if runner.data >= value:
            runner_prev = runner
        else:
            new = Node(runner.data)
            new.next = head
            llist.head = new
            head = llist.head
            runner_prev.next = runner.next

    return llist

# Solution 2:
# O(N)
def partition_alt(llist, value):
    new = Node(llist.head.data)
    part_list = SLinkedList(new)
    head = part_list.head
    tail = part_list.head

    current = llist.head.next
    while current is not None:
        next_node = current.next
        if current.data >= value:
            tail.next = current
            tail = current
        else:
            current.next = head
            head = current

        current = next_node

    tail.next = None
    part_list.head = head
    
    return part_list

# Testing
class Tests(unittest.TestCase):

    def test_partition_at_head(self):
        llist = SLinkedList()
        llist.add_multi(5, 8, 3, 5, 10, 2, 1)
        self.assertEqual(partition(llist, 5).data_list(), [1,2,3,'*',5,8,5,10])
    
    def test_partition_not_at_head(self):
        llist = SLinkedList()
        llist.add_multi(3, 5, 8, 5, 10, 2, 1)
        self.assertEqual(partition(llist, 5).data_list(), [1,2,3,'*',5,8,5,10])
    
    def test_partition_alt(self):
        llist = SLinkedList()
        llist.add_multi(3, 6, 7, 4, 3, 8, 5, 6, 2)
        self.assertEqual(partition_alt(llist, 5).data_list(), [2,3,4,3,6,7,8,5,6])

if __name__ == '__main__':
    unittest.main()
