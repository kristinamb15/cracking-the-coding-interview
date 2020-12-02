# 2.2 Return Kth to Last: implement an algorithm to find teh kth to last element of a singly linked list.

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
    print(str(kth))

example1 = SLinkedList()
example1.add_multi(1, 2, 3, 4, 5)
kth_to_last(example1, 2)