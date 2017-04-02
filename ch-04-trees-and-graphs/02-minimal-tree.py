# Create a minimal height binary search tree with the elements of a given
# sorted array.

def minimal_height_bst(sorted_array):
  if len(sorted_array) == 0:
    return None
  middle = len(sorted_array) / 2
  left  = minimal_height_bst(sorted_array[:middle])
  right = minimal_height_bst(sorted_array[(middle+1):])
  return BSTNode(sorted_array[middle], left, right)

class BSTNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right

  def __str__(self):
    string = "(" + str(self.data)
    if self.left:  string += str(self.left)
    else:          string += "."
    if self.right: string += str(self.right)
    else:          string += "."
    return string + ")"

import unittest

class Test(unittest.TestCase):
  def test_minimal_height_bst(self):
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bst = minimal_height_bst(sorted_array)
    self.assertEqual(str(bst), "(5(3(2(1..).)(4..))(8(7(6..).)(9..)))")

if __name__ == "__main__":
  unittest.main()

