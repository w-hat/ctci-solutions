# Return the bounds of the minimal portion of an array would make the entire
# array sorted if it were sorted.

def sub_sort(array):
  n = len(array)
  if n == 0:
    return (0, 0)
  min_so_far = [0] * n
  max_so_far = [0] * n
  max_so_far[0] = array[0]
  for i in xrange(1, n):
    max_so_far[i] = max(array[i], max_so_far[i - 1])
  min_so_far[-1] = array[-1]
  for i in xrange(n - 2, -1, -1):
    min_so_far[i] = min(array[i], min_so_far[i + 1])
  start, end = 0, n - 1
  while end > 0 and min_so_far[end] == max_so_far[end]:
    end -= 1
  while start < end and min_so_far[start] == max_so_far[start]:
    start += 1
  return (start, end)

import unittest

class Test(unittest.TestCase):
  def test_sub_sort(self):
    array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    self.assertEqual(sub_sort(array), (0, 0))
    array = [10, 11, 12, 13, 14, 16, 15, 17, 18, 19]
    self.assertEqual(sub_sort(array), (5, 6))
    array = [10, 18, 12, 13, 14, 16, 15, 17, 11, 19]
    self.assertEqual(sub_sort(array), (1, 8))
    array = [90, 80, 70, 60, 50, 40, 30, 20, 10, 01]
    self.assertEqual(sub_sort(array), (0, 9))

if __name__ == "__main__":
  unittest.main()

