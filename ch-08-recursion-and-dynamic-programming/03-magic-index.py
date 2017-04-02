# Find a magic index in a sorted array.

def magic_index_distinct(array):
  if len(array) == 0 or array[0] > 0 or array[-1] < len(array) - 1:
    return None
  return magic_index_distinct_bounds(array, 0, len(array))

def magic_index_distinct_bounds(array, lower, upper):
  if lower == upper:
    return None
  middle = (lower + upper) / 2
  if array[middle] == middle:
    return middle
  elif array[middle] > middle:
    return magic_index_distinct_bounds(array, lower, middle)
  else:
    return magic_index_distinct_bounds(array, middle+1, upper)

def magic_index(array):
  index = 0
  while index < len(array):
    if index == array[index]:
      return index
    index = max(array[index], index + 1)
  return None

import unittest

class Test(unittest.TestCase):
  def test_magic_index_distinct(self):
    self.assertEqual(magic_index_distinct([3,4,5]), None)
    self.assertEqual(magic_index_distinct([-2,-1,0,2]), None)
    self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,6,20]), None)
    self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,7,20]), 7)
    self.assertEqual(magic_index_distinct([-20,1,2,3,4,5,6,20]), 4)
  
  def test_magic_index(self):
    self.assertEqual(magic_index([3,4,5]), None)
    self.assertEqual(magic_index([-2,-1,0,2]), None)
    self.assertEqual(magic_index([-20,0,1,2,3,4,5,6,20]), None)
    self.assertEqual(magic_index([-20,0,1,2,3,4,5,7,20]), 7)
    self.assertEqual(magic_index([-20,1,2,3,4,5,6,20]), 1)
    self.assertEqual(magic_index([-20,5,5,5,5,5,6,20]), 5)

if __name__ == "__main__":
  unittest.main()

