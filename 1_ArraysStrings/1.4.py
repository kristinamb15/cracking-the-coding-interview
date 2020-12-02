# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# The palindrome does not need to be limited to just dictionary words.
# You can ignore casing and non-letter characters.

import unittest

# Solution 1
# O(N)
def palindrome_perm(mystring):
    mystring = mystring.lower()
    char_dict = {char:0 for char in mystring if char.isalpha()}
    for char in mystring:
        if char.isalpha():
            char_dict[char] += 1
    evens = 0
    odds = 0
    for key in char_dict:
        if char_dict[key] % 2 == 0:
            evens += 1
        else:
            odds += 1
    result = (odds == 1 or odds == 0)
    return result

# Testing
class Tests(unittest.TestCase):
    
    def test_with_space_true(self):
        self.assertTrue(palindrome_perm('taco cat'))
    
    def test_with_space_false(self):
        self.assertFalse(palindrome_perm('I am not a palindrome'))
    
    def test_no_space_true(self):
        self.assertTrue(palindrome_perm('racecar'))
    
    def test_no_space_false(self):
        self.assertFalse(palindrome_perm('nope'))
    
    def test_with_punc_true(self):
        self.assertTrue(palindrome_perm('Was it a cat I saw?'))  

if __name__ == '__main__':
    unittest.main()
                