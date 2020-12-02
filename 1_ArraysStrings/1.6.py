# 1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# Ex: aabcccccaaa would become a2b1c5a3
# If the compressed string is not smaller than the original, your method should return the original.
# Assume the string is only uppercase and lowercase letters a-z.

import unittest

class MyString:
    def __init__(self, mystring):
        self.mystring = mystring
    
    # Solution 1
    # O(N)
    def compress_string(self):
        mydict = {i: 0 for i in range(len(self.mystring))}

        curr_index = 0
        for i in range(len(self.mystring)):
            if self.mystring[curr_index]  == self.mystring[i]:
                mydict[curr_index] += 1
            else:
                curr_index = i
                mydict[curr_index] += 1       

        comp_str = ''
        for index, count in mydict.items():
            if count != 0:
                comp_str += self.mystring[index] + str(count)
        if len(self.mystring) <= len(comp_str):
            result = self.mystring
        else:
            result = comp_str
        return result

# Testing
class Tests(unittest.TestCase):
    
    def test_compress_string_new(self):
        test_str = MyString('aabcccccaaa')
        self.assertEqual(test_str.compress_string(), 'a2b1c5a3')
    
    def test_compress_string_same(self):
        test_str = MyString('aab')
        self.assertEqual(test_str.compress_string(), 'aab')

if __name__ == '__main__':
    unittest.main()