# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

from trees import (Node, Tree)

# Solution 1:
# O(NlogN) ???
def create_min_tree(arr):
    new_node = Node(arr, True)
    new_tree = Tree(new_node)
    create_subtree(new_tree, new_tree.root)
    new_tree.print_bf()

def create_subtree(tree, subroot):
    if subroot.data is not None:
        arr = subroot.data
        parent_index = len(arr) // 2
        parent_data = arr[parent_index]
     
        left_data = [value for value in arr if value < parent_data]
        right_data = [value for value in arr if value > parent_data]
        right_data.sort(reverse=True)
            
        if len(left_data) == 0:
            left_data = None
        if len(right_data) == 0:
            right_data = None

        subroot.data = parent_data
        if left_data is not None:
            left = Node(left_data, True)
            subroot.add_child(left, True, False)
            create_subtree(tree, left)
        if right_data is not None:
            right = Node(right_data, True)
            subroot.add_child(right, False, True)
            create_subtree(tree, right)      
        

ex1_array = [2, 4, 6, 8, 10, 20]
create_min_tree(ex1_array)