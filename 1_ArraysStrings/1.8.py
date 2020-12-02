# 1.8 Zero Matrix: Wrtie an alogrithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

import unittest

# Solution 1:
# O(MN)
def zero_rows(matrix):
    zero_rows = set()
    zero_cols = set()
    for row in matrix:
        for item in row:
            if item == 0:
                zero_cols.add(row.index(item))
                zero_rows.add(matrix.index(row))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in zero_rows:
                matrix[i][j] = 0
            elif j in zero_cols:
                matrix[i][j] = 0

    return matrix

# Testing
class Tests(unittest.TestCase):
    
    def test_zero_rows_2(self):
        test_matrix = [[1, 0], [2, 3]]
        self.assertEqual(zero_rows(test_matrix), [[0, 0], [2, 0]])
    
    def test_zero_rows_3(self):
        test_matrix = [[1, 2, 0], [4, 5, 6], [7, 0, 9]]
        self.assertEqual(zero_rows(test_matrix), [[0, 0, 0], [4, 0, 0], [0, 0, 0]])

if __name__ == '__main__':
    unittest.main()
