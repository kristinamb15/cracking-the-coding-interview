# 1.3 URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the 'true' length of the string.
# Ex: Input is "Mr John Smith  ", 13; Output is "Mr%20John%20Smith"

import unittest

class MyString:
    def __init__(self, mystring):
        self.mystring = mystring
    
    # Solution 1: a bit too easy as the replace method is built in
    # O(N)
    def urlify(self):
        newstring = self.mystring.replace(' ', '%20')
        return newstring

    # Solution 2
    # O(N)
    def urlify_alt(self):
        newstring = ''
        for char in self.mystring:
            if char != ' ':
                newstring += char
            else:
                newstring += '%20'
        return newstring
    
    # Solution 3 - no new string
    # O(N)
    def urlify_alt2(self):
        str_arr = self.mystring.split(' ')
        self.mystring = '%20'.join(str_arr)
        return self.mystring

# Testing
class Tests(unittest.TestCase):
    def setUp(self):
        self.mystring = MyString('This is my string')
        self.url = 'This%20is%20my%20string'
    
    def test_urlify(self):
        self.assertEqual(self.mystring.urlify(), self.url)
    
    def test_urlify_alt(self):
        self.assertEqual(self.mystring.urlify(), self.url)
    
    def test_urlify_alt2(self):
        self.assertEqual(self.mystring.urlify(), self.url)

if __name__ == '__main__':
    unittest.main()

