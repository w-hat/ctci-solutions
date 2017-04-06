# Return the pairs with a given sum.

def pairs_with_sum(arr, s):
  values = set()
  for elem in arr:
    values.add(elem)
  pairs = set()
  for elem in arr:
    if (s - elem) in values:
      values.remove(elem)
      pairs.add((elem, s - elem))
  return pairs

import unittest

class Test(unittest.TestCase):
  def test_pairs_with_sum(self):
    arr = [2, 3, 4, 11, -4]
    self.assertEqual(pairs_with_sum(arr, 7), {(3,4),(11,-4)})
    arr = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 20, 30, -11]
    self.assertEqual(pairs_with_sum(arr, 55), {(0,55),(22,33),(66,-11),(11,44)})

if __name__ == "__main__":
  unittest.main()

