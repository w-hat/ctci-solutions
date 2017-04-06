# Return the index of two numbers which could be swapped to make the sum of
# the two arrays equal.

def equalize_sum_with_swap(arr1, arr2):
  sum1, sum2 = sum(arr1), sum(arr2)
  if (sum1 - sum2) % 2:
    return None
  target_diff = (sum1 - sum2) / 2
  elems = {}
  for i, elem in enumerate(arr1):
    elems[elem - target_diff] = i
  for i, elem in enumerate(arr2):
    if elem in elems:
      return (elems[elem], i)
  return None

import unittest

class Test(unittest.TestCase):
  def test_equalize_sum_with_swap(self):
    arr1 = [5, 5, 10]
    arr2 = [4, 4, 8]
    swap = equalize_sum_with_swap(arr1, arr2)
    self.assertEqual(swap, (2, 2))
    arr1 = [5, 5, 5]
    arr2 = [6, 4, 6]
    swap = equalize_sum_with_swap(arr1, arr2)
    self.assertEqual(swap, None)
    arr1 = [5, 5, 14]
    arr2 = [7, 7, 8]
    swap = equalize_sum_with_swap(arr1, arr2)
    self.assertEqual(swap, None)
    arr1 = [5, 5, 14]
    arr2 = [4, 10, 8]
    swap = equalize_sum_with_swap(arr1, arr2)
    self.assertEqual(swap, (1, 0))

if __name__ == "__main__":
  unittest.main()

