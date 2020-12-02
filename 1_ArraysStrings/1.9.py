# 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, check if s2 is a rotation of s1 using only one call to isSubstring.
# Ex: 'waterbottle' is a rotation of 'erbottlewat'

import unittest

# Solution 1: Didn't actually use substring check
# O(N)

def chars_diff(str1, str2):
    str1_chars = sorted(list(str1.lower()))
    str2_chars = sorted(list(str2.lower()))

    return str1_chars != str2_chars

def str_rotation(str1, str2):
    if chars_diff(str1, str2):
        result = False
    else:
        start = str1.index(str2[0])
        new_str = str1[start:] + str1[0:start]
    if new_str == str2:
        result = True
    else:
        result = False
    return result

# Solution 2
# O(N)
def str_rotation_alt(str1, str2):
    if chars_diff(str1, str2):
        result = False
    else:
        for i in range(len(str1)):
            if str1[i:] in str2:
                result = True
                break
            else:
                result = False
    return result

# Solution 3: The best way - after looking at solutions
# O(N)
def str_rotation_best(str1, str2):
    if chars_diff(str1, str2):
        result = False
    else:
        result = str2 in str1 + str1
    return result

# Testing
class Tests(unittest.TestCase):
    def setUp(self):
        self.test_string = 'waterbottle'
        self.test_string_r = 'erbottlewat'
    
    def test_rotation_true(self):
        self.assertTrue(str_rotation(self.test_string, self.test_string_r))
    
    def test_rotation_alt_true(self):
        self.assertTrue(str_rotation_alt(self.test_string, self.test_string_r))
    
    def test_rotation_best_true(self):
        self.assertTrue(str_rotation_best(self.test_string, self.test_string_r))

if __name__ == '__main__':
    unittest.main()