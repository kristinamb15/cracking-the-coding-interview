# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

from trees import (Node, Tree)

import unittest

# Solution 1:
# O(NlogN) ???
def create_min_tree(arr):
    new_node = Node(arr, True)
    new_tree = Tree(new_node)
    create_subtree(new_tree, new_tree.root)
    return new_tree

# Appends a subtree to a given tree at a given subroot
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

# Testing
class Tests(unittest.TestCase):

    def setUp(self):
        self.test_array = [2, 4, 6, 8, 10, 20]
        self.min_tree = create_min_tree(self.test_array)

    def test_create_min_tree(self):
        self.assertEqual(self.min_tree.root.data, 8)
        self.assertEqual(self.min_tree.root.left.data, 4)
        self.assertEqual(self.min_tree.root.right.data, 10)
        self.assertEqual(self.min_tree.root.left.left.data, 2)
        self.assertEqual(self.min_tree.root.left.right.data, 6)
        self.assertIsNone(self.min_tree.root.right.left)
        self.assertEqual(self.min_tree.root.right.right.data, 20)

if __name__ == '__main__':
    unittest.main()