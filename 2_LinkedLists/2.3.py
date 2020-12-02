# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (any node but the first and last),
# given only access to that node
# Ex: delete c from a, b, c, d, e, f

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

# Solution 2: without invoking the list at all
# O(1)
def delete_mid_alt(el):
    if el is None or el.next is None:
        return False
    else:
        el.data = el.next.data
        el.next = el.next.next

example1 = SLinkedList()
example1.add_multi(1, 5, 9, 12)
delete_mid(example1, 9)
example1.pretty_print()

example2 = SLinkedList()
example2.add_multi(1, 3, 4, 5, 6, 8, 3, 4)
delete_mid(example2, 4)
example2.pretty_print()

node1 = Node(1)
node5 = Node(5)
node9 = Node(9)
node12 = Node(12)

node1.next = node5
node5.next = node9
node9.next = node12
example3 = SLinkedList(node1)
example3.pretty_print()
delete_mid_alt(node9)
example3.pretty_print()