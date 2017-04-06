# Return the bounds of the contiguous sequence with the largest sum.

def contiguous_sequence(array):
  if len(array) == 0:
    return None
  largest_bounds = (0, 0)
  largest_sum = 0
  reach_start = 0
  reach_sum = 0
  for i, elem in enumerate(array):
    reach_sum += elem
    if reach_sum < 0:
      reach_sum = 0
      reach_start = i + 1
    if reach_sum > largest_sum:
      largest_sum = reach_sum
      largest_bounds = (reach_start, i + 1)
  return largest_bounds

import unittest

class Test(unittest.TestCase):
  def test_contiguous_sequence(self):
    seq = [-1, 4, 4, -7, 8, 2, -4, 3]
    self.assertEqual(contiguous_sequence(seq), (1, 6))
    seq = [-1, 4, 4, -7, 8, 2, -4, -3, 9]
    self.assertEqual(contiguous_sequence(seq), (1, 9))
    seq = [-1, -4, -54, -7, -8, 2, -4, -3, 9]
    self.assertEqual(contiguous_sequence(seq), (8, 9))
    seq = [-1, -4, -54, -7, -8, -2, -4, -3, -9]
    self.assertEqual(contiguous_sequence(seq), (0, 0))

if __name__ == "__main__":
  unittest.main()

