# 1.5 One Away: There are three types of edits than can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

import unittest

# Solution 1
# O(N)
def one_away(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = {char:0 for char in str1}
    dict2 = {char:0 for char in str2}

    for char in str1:
        dict1[char] += 1
    for char in str2:
        dict2[char] += 1

    diff = 0

    if abs(len(str1) - len(str2)) > 1:
        result = False;

    else:
        if len(str1) > len(str2):
            larger = dict1
            smaller = dict2
        else:
            larger = dict2
            smaller = dict1
        for key in larger.keys():
            if key in smaller.keys():
                if larger[key] != smaller[key]:
                    diff += 1
            else:
                diff += 1

    result = diff <= 1
    return (result,diff)

# Testing
class Tests(unittest.TestCase):
    
    def test_true_diff_length(self):
        self.assertEqual(one_away('pale', 'ale'), (True,1))
    
    def test_true_same_length(self):
        self.assertEqual(one_away('bale', 'pale'), (True,1))
    
    def test_false(self):
        self.assertEqual(one_away('bale', 'gal'), (False,2))

if __name__ == '__main__':
    unittest.main()