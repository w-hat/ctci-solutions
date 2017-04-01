# Merge array b into array a given that array a contains len(b) extra space at
# the end.

def sorted_merge(a, b):
  bix = len(b) - 1
  aix = len(a) - len(b) - 1
  while aix >= 0 and bix >= 0:
    if a[aix] > b[bix]:
      a[aix + bix + 1] = a[aix]
      aix -= 1
    else:
      a[aix + bix + 1] = b[bix]
      bix -= 1
  while bix >= 0:
    a[bix] = b[bix]
    bix -= 1

import unittest

class Test(unittest.TestCase):
  def test_sorted_merge(self):
    a = [33, 44, 55, 66, 88, 99, None, None, None]
    b = [11, 22, 77]
    sorted_merge(a, b)
    self.assertEqual(a, [11, 22, 33, 44, 55, 66, 77, 88, 99])
    a = [11, 22, 55, 66, 88, None, None, None]
    b = [33, 44, 99]
    sorted_merge(a, b)
    self.assertEqual(a, [11, 22, 33, 44, 55, 66, 88, 99])

if __name__ == "__main__":
  unittest.main()

