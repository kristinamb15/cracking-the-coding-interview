# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

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
    
    print(str(result))

example1 = SLinkedList()
example1.add_multi(1, 2, 3, 4, 5)
palindrome(example1) # False

example2 = SLinkedList()
example2.add_multi(1, 2, 3, 2, 1)
palindrome(example2) # True