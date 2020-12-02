# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit, stored in reverse order.
# Write a function that adds the two numbers and returns the sum as a linked list.
# You cannot just convert the linked list to an integer.
# Follow up: Suppose the digits are stored in forward order

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
    result.pretty_print()

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
    partial_result = SLinkedList()
    while cur1 is not None:
        sums = cur1.data + cur2.data
        if sums >= 10:
            extra.add_node(1)
            sums = sums - 10
        else:
            extra.add_node(0)
        partial_result.add_node(sums)
        cur1 = cur1.next
        cur2 = cur2.next
    extra.add_node(0)

    if check_zero(extra):
        partial_result.pretty_print()
    else:
        sum_lists_forward(extra, partial_result)


def check_zero(llist):
    is_zero = True
    current = llist.head
    while current is not None:
        if current.data != 0:
            is_zero = False
            break
        current = current.next
    return is_zero

example1a = SLinkedList()
example1a.add_multi(7, 1, 6, 1)
example1b = SLinkedList()
example1b.add_multi(5, 9, 2)
sum_lists(example1a, example1b) # 2, 1, 9, 1

example2a = SLinkedList()
example2a.add_multi(5, 1, 8)
example2b = SLinkedList()
example2b.add_multi(5, 4, 3)
sum_lists(example2a, example2b) # 0, 6, 1, 1

sum_lists_forward(example1a, example1b) # 0, 7, 7, 5, 3