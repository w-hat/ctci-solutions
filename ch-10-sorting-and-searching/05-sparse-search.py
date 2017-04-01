# Search a sorted sparse array of positive integers.

def sparse_search(array, item):
  if item < 1:
    return None
  return sparse_search_bounds(array, item, 0, len(array))

def sparse_search_bounds(array, item, left_ix, right_ix):
  if left_ix == right_ix:
    return None
  middle_ix = (left_ix + right_ix) / 2
  next_ix = middle_ix
  next = array[next_ix]
  while not next:
    next_ix += 1
    if next_ix == len(array):
      return sparse_search_bounds(array, item, left_ix, middle_ix)
    next = array[next_ix]
  if next == item:
    return next_ix
  if next > item:
    return sparse_search_bounds(array, item, left_ix, middle_ix)
  else:
    return sparse_search_bounds(array, item, next_ix+1, right_ix)

import unittest

class Test(unittest.TestCase):
  def test_sparse_search(self):
    array = [0, 0, 7, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 37, 40, 0, 0, 0]
    self.assertEqual(sparse_search(array, 0), None)
    self.assertEqual(sparse_search(array, 7), 2)
    self.assertEqual(sparse_search(array, 19), 8)
    self.assertEqual(sparse_search(array, 37), 13)
    self.assertEqual(sparse_search(array, 40), 14)
    array = [0, 12, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    self.assertEqual(sparse_search(array, 12), 1)
    self.assertEqual(sparse_search(array, 18), 3)

if __name__ == "__main__":
  unittest.main()

