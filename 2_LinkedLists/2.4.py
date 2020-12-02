# 2.4 Partition: Write code to partition a linked list around a value x, such that ll nodes less than x come before all nodes greater than or equal to x.
# The partition element x can be anywhere in the "right partition" - it doesn't have to be in the middle
# Ex: 3, 5, 8, 5, 10, 2, 1 becomes 3, 1, 2, 10, 5, 5, 8

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


example1 = SLinkedList()
example1.add_multi(3, 5, 8, 5, 10, 2, 1)
partition(example1, 5)
example1.pretty_print()

example2 = SLinkedList()
example2.add_multi(5, 8, 3, 5, 10, 2, 1)
partition(example2, 5)
example2.pretty_print()

example3 = SLinkedList()
example3.add_multi(3, 6, 7, 4, 3, 8, 5, 6, 2)
example3_part = partition_alt(example3, 5)
example3_part.pretty_print()
