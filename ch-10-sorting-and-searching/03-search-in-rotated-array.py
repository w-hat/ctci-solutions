# Search for an item in a rotated array.

def rotated_search(array, item, leftix=0, rightix=None):
  if rightix is None:
    rightix = len(array)
  if rightix <= leftix:
    return None
  middleix = (rightix + leftix) / 2
  left, middle = array[leftix], array[middleix]
  if item == middle:
    return middleix
  if item == left:
    return leftix
  if left > middle:
    if middle < item and item < left:
      return rotated_search(array, item, middleix+1, rightix)
    else:
      return rotated_search(array, item, leftix+1, middleix)
  elif left < item and item < middle:
    return rotated_search(array, item, leftix+1, middleix)
  else:
    return rotated_search(array, item, middleix+1, rightix)

import unittest

class Test(unittest.TestCase):
  def test_rotated_search(self):
    array = [55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45]
    self.assertEqual(rotated_search(array, 55), 0)
    self.assertEqual(rotated_search(array, 60), 1)
    self.assertEqual(rotated_search(array, 90), 7)
    self.assertEqual(rotated_search(array, 95), 8)
    self.assertEqual(rotated_search(array, 15), 9)
    self.assertEqual(rotated_search(array, 30), 12)
    self.assertEqual(rotated_search(array, 45), 15)

if __name__ == "__main__":
  unittest.main()

