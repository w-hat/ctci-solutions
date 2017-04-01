# Search a sorted martix.

def sorted_matrix_search(mat, item):
  if len(mat) == 0:
    return None
  return sorted_matrix_search_bounds(mat, item, 0, len(mat[0]), 0, len(mat))

def sorted_matrix_search_bounds(mat, item, x1, x2, y1, y2):
  if x1 == x2 or y1 == y2:
    return None
  row, col = (y1 + y2)/2, (x1 + x2)/2
  middle = mat[row][col]
  if middle == item:
    return (row, col)
  if middle > item:
    found = sorted_matrix_search_bounds(mat, item, x1, col, y1, row) or \
            sorted_matrix_search_bounds(mat, item, col, col+1, y1, row) or \
            sorted_matrix_search_bounds(mat, item, x1, col, row, row+1)
    if found:
      return found
  else:
    found = sorted_matrix_search_bounds(mat, item, col+1, x2, row+1, y2) or \
            sorted_matrix_search_bounds(mat, item, col, col+1, row+1, y2) or \
            sorted_matrix_search_bounds(mat, item, col+1, x2, row, row+1)
    if found:
      return found
  return sorted_matrix_search_bounds(mat, item, x1, col, row+1, y2) or \
         sorted_matrix_search_bounds(mat, item, col+1, x2, y1, row)

import unittest

class Test(unittest.TestCase):
  def test_sorted_matrix_search(self):
    mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
           [5,  10, 15, 20, 25, 30, 35, 40, 45],
           [10, 20, 30, 40, 50, 60, 70, 80, 90],
           [13, 23, 33, 43, 53, 63, 73, 83, 93],
           [14, 24, 34, 44, 54, 64, 74, 84, 94],
           [15, 25, 35, 45, 55, 65, 75, 85, 95],
           [16, 26, 36, 46, 56, 66, 77, 88, 99]]
    self.assertEqual(sorted_matrix_search(mat, 10), (1,1))
    self.assertEqual(sorted_matrix_search(mat, 13), (3,0))
    self.assertEqual(sorted_matrix_search(mat, 14), (4,0))
    self.assertEqual(sorted_matrix_search(mat, 16), (6,0))
    self.assertEqual(sorted_matrix_search(mat, 56), (6,4))
    self.assertEqual(sorted_matrix_search(mat, 65), (5,5))
    self.assertEqual(sorted_matrix_search(mat, 74), (4,6))
    self.assertEqual(sorted_matrix_search(mat, 99), (6,8))

if __name__ == "__main__":
  unittest.main()

