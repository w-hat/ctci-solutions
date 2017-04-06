# Find the smallest difference between any two elements of two arrays.

# Of course an O(n*lg(n) + m*lg(n)) solutions exists in which we only sort
# one array and search through it for the closest to each element of the other,
# but this O(n*lg(n) + m*lg(m)) solution feels more simple.
# And, sometimes at least, simplicity counts for something.

# Also, there is an O(d*n + m) solution where d is the smallest difference
# found between a constant number of terms at the beginning of the two arrays.
# This solution would continue by storing d items in a hash table for each
# element in the first array.

def smallest_difference(array1, array2):
  if len(array1) == 0 or len(array2) == 0:
    return None
  sorted1, sorted2 = sorted(array1), sorted(array2)
  smallest_diff = abs(sorted1[0] - sorted2[0])
  ix1, ix2 = 0, 0
  while True:
    diff = sorted1[ix1] - sorted2[ix2]
    smallest_diff = min(smallest_diff, abs(diff))
    if diff == 0:
      break
    if diff < 0:
      ix1 += 1
      if ix1 == len(sorted1):
        break
    else:
      ix2 += 1
      if ix2 == len(sorted2):
        break
  return smallest_diff

import unittest

class Test(unittest.TestCase):
  def test_smallest_difference(self):
    self.assertEqual(smallest_difference([11, 22, 33, 44], [77, 2, 66, 50]), 6)
    self.assertEqual(smallest_difference([11, 22, 33, 44], [77, 2, 34, 50]), 1)
    self.assertEqual(smallest_difference([11, 77, 33, 44], [77, 2, 34, 50]), 0)
    array1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    array2 = [33, 45, 58, 17]
    self.assertEqual(smallest_difference(array1, array2), 2)
    self.assertEqual(smallest_difference(array2, array1), 2)

if __name__ == "__main__":
  unittest.main()

