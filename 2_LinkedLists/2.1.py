from linked_list import (Node, SLinkedList)

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# Follow up: How would you solve this problem if a temporary buffer is not allowed?

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

def run_examples():
    print('\nExample 1:')
    example1 = SLinkedList()
    example1.add_multi(2, 1, 3, 2, 4)
    example1.pretty_print()
    remove_dups(example1)
    example1.pretty_print()

    print('\nExample 2:')
    example2 = SLinkedList()
    example2.add_multi(1, 3, 5, 3, 2, 4)
    example2.pretty_print()
    remove_dups_alt(example2)
    example2.pretty_print()

    print('\nExample 3:')
    example3 = SLinkedList()
    example3.add_multi(1, 2, 3, 4, 5, 3, 2)
    example3.pretty_print()
    remove_dups_ideal(example3)
    example3.pretty_print()

if __name__ == '__main__':
    run_examples()
