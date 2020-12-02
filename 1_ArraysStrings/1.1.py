# 1.1 Is Unique: implement an alogorithim to determine if a string has all unique characters. What if you can't use additional data structures?

import unittest
import string

# Solution 1: does not use additional data structures
# O(N^2)
def is_unique(mystring):
    for i in range(len(mystring) + 1):
        for char in mystring[i + 1:]:
            if mystring[i] == char:
                return False
    return True

# Solution 2: using additional data structures (set)
# O(N) amortized to O(1)
def is_unique_2(mystring):
    char_list = set(mystring)
    if len(char_list) == len(mystring):
        return True
    return False

# Testing
class Tests(unittest.TestCase):
    def test_is_unique_true(self):
        self.assertTrue(is_unique('snake'))
    
    def test_is_unique_false(self):
        self.assertFalse(is_unique('unique'))
    
    def test_is_unique_2_true(self):
        self.assertTrue(is_unique('snake'))
    
    def test_is_unique_2_false(self):
        self.assertFalse(is_unique('unique'))

if __name__ == '__main__':
    unittest.main()