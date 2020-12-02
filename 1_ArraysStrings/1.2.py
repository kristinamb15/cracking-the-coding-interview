# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

import unittest

class MyString:
    def __init__(self, mystring):
        self.mystring = mystring

    # Solution 1: using sorted list
    # O(N log N)
    def is_perm1(self, other_string):
        list1 = list(self.mystring)
        list2 = list(other_string)
        result = (sorted(list1) == sorted(list2))
        return result
    
    # Solution 2: using a dictionary
    # O(N)
    def is_perm2(self, other_string):
        if len(other_string) != len(self.mystring):
            result = False
        else:
            dict_other = {char:0 for char in other_string}
            dict_mine = {char:0 for char in self.mystring}
            for char in self.mystring:
                dict_mine[char] += 1
            for char in other_string:
                dict_other[char] += 1
            if dict_mine.keys() != dict_other.keys():
                result = False
            else:
                for key in dict_mine.keys():
                    if dict_mine[key] == dict_other[key]:
                        result = True
                    else:
                        result = False
            return result

# Testing
class Tests(unittest.TestCase):
    def setUp(self):
        self.cabbage = MyString('cabbage')

    def test_is_perm1_true(self):
        self.assertTrue(self.cabbage.is_perm1('bacbage'))
    
    def test_is_perm1_false(self):
        self.assertFalse(self.cabbage.is_perm1('baggage'))
    
    def test_is_perm2_true(self):
        self.assertTrue(self.cabbage.is_perm2('bacbage'))
    
    def test_is_perm2_false(self):
        self.assertFalse(self.cabbage.is_perm2('baggage'))

if __name__ == '__main__':
    unittest.main()