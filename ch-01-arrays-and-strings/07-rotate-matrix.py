# Rotate a square matrix by 90 degrees counter-clockwise about its center.

# TODO Use a matrix instead of a two-dimensional list.

import unittest

def rotate_matrix(m):
  n = len(m)
  rotm = [None] * n
  for row in xrange(n):
    rotm[row] = [None] * n
  for row in xrange(n):
    for col in xrange(n):
      rotm[n - col - 1][row] = m[row][col]
  return rotm

def rotate_matrix_in_place(m):
  n = len(m)
  for col in xrange(n/2):
    for row in xrange(col, n - col - 1):
      temp1 = m[n - col - 1][row]
      m[n - col - 1][row] = m[row][col]
      temp2 = m[n - row - 1][n - col - 1]
      m[n - row - 1][n - col - 1] = temp1
      temp1 = m[col][n - row - 1]
      m[col][n - row - 1] = temp2
      m[row][col] = temp1

class Test(unittest.TestCase):
  def test_rotate_matrix(self):
    mat1 = [[1,2],[3,4]]
    mat2 = [[2,4],[1,3]]
    self.assertEqual(rotate_matrix(mat1), mat2)
    mat3 = [[1,2,3],[4,5,6],[7,8,9]]
    mat4 = [[3,6,9],[2,5,8],[1,4,7]]
    self.assertEqual(rotate_matrix(mat3), mat4)
    mat5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    mat6 = [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]
    self.assertEqual(rotate_matrix(mat5), mat6)
  
  def test_rotate_matrix_in_place(self):
    mat1 = [[1,2],[3,4]]
    mat2 = [[2,4],[1,3]]
    rotate_matrix_in_place(mat1)
    self.assertEqual(mat1, mat2)
    mat3 = [[1,2,3],[4,5,6],[7,8,9]]
    mat4 = [[3,6,9],[2,5,8],[1,4,7]]
    rotate_matrix_in_place(mat3)
    self.assertEqual(mat3, mat4)
    mat5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    mat6 = [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]
    rotate_matrix_in_place(mat5)
    self.assertEqual(mat5, mat6)

if __name__ == "__main__":
  unittest.main()
