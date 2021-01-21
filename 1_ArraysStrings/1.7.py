# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degrres.
# Can you do this in place?

import unittest
import numpy as np

class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.columns = [[row[i] for row in self.rows] for i in range(len(self.rows))]

    # Best Solution: in place - can be used on any list of lists
    # O(N^2)
    def rotate_90_best(self):
        for i in range(self.rows[0]):
            for row in self.rows[::-1]:
                self.rows[i].append(row.pop(0))

    # Solution 1: not in place: created a new list of rows
    # O(N^2)
    def rotate_90(self):
        n = len(self.rows)
        new = [[] for row in self.rows]
        i = n - 1
        while i >= 0:
            row = self.rows[i]
            for j in range(len(row)):
                new[j].append(row[j])
            i -= 1
        return new
    
    # Solution 2: in place (using columns)
    # O(N^2)
    def rotate_90_in_place(self):
        self.rows = [column[::-1] for column in self.columns]
        return self.rows
    
    # Solution 3: matrix multiplication (my favorite!)
    # O(N^2)
    def rotate_multiply(self):
        n = len(self.rows)
        rotate_matrix = [[0 for i in range(n)] for row in range(n)]
        i = n - 1
        while i >= 0:
            rotate_matrix[n - 1 - i][i] = 1
            i -= 1
            
        new = np.transpose(np.dot(rotate_matrix, self.rows)).tolist()
        return new

# Testing
class Tests(unittest.TestCase):
    def setUp(self):
        self.my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.result = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    def test_rotate_90_best(self):
        self.assertEqual(self.my_matrix.rotate_90(), self.result)

    def test_rotate_90(self):
        self.assertEqual(self.my_matrix.rotate_90(), self.result)
    
    def test_rotate_90_in_place(self):
        self.assertEqual(self.my_matrix.rotate_90_in_place(), self.result)
    
    def test_rotate_multiply(self):
        self.assertEqual(self.my_matrix.rotate_multiply(), self.result)

if __name__ == '__main__':
    unittest.main()