# 2.8 Loop Detection: Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists)

from linked_list import (Node, SLinkedList)


# Solution 1
# O(N) - where N is the length up to the loop
def find_loop(llist):
    curr = llist.head
    already = []
    while curr not in already and curr is not None:
        already.append(curr)
        curr = curr.next
    if curr is None:
        print('No loops.')
    else:
        print('Loop at: ' + str(curr.data))

# Solution 2
# O(N) where N is length of loop ?

def find_loop_alt(llist):
    slow_runner = llist.head
    fast_runner = llist.head

    while (fast_runner is not None) and (fast_runner.next is not None):
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner == fast_runner:
            loop = True
            break
        else:
            loop = False
    
    if loop:    
        slow_runner = llist.head
        while slow_runner != fast_runner:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next
    
    if loop:
        print('Loop at: ' + str(fast_runner.data))
    else:
        print('No loops')
        


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeC

list1 = SLinkedList(nodeA)
list2 = SLinkedList()
list2.add_multi(1, 2, 3, 4, 5)

find_loop(list1)
find_loop(list2)

find_loop_alt(list1)
find_loop_alt(list2)
