# Given a matrix, zero out every row and column that contains a zero.

import unittest

def zero_out_row_col(mat):
  n = len(mat)
  if n == 0:
    return mat
  m = len(mat[0])
  zero_rows, zero_cols = [], []
  for r in xrange(n):
    for c in xrange(m):
      if mat[r][c] == 0:
        zero_rows.append(r)
        zero_cols.append(c)
        break
  for r in zero_rows:
    for c in xrange(m):
      mat[r][c] = 0
  for c in zero_cols:
    for r in xrange(n):
      mat[r][c] = 0

class Test(unittest.TestCase):
  def test_zero_out_row_col_matrix(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
    zero_out_row_col(mat1)
    self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()
