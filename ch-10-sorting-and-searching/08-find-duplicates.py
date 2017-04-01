# Find the duplicates in an array that contains numbers between 0 and 32000.

def find_duplicates(array):
  bv = [0] * 512
  duplicates = []
  for n in array:
    bit = 1 << (n % 64)
    if bv[n / 64] & bit:
      duplicates.append(n)
    else:
      bv[n / 64] |= bit
  return duplicates

import unittest

class Test(unittest.TestCase):
  def test_find_duplicates(self):
    array = [1, 2, 3, 4, 55, 20000, 20001, 20002, 20003, 17, 18, 19, 20, 22, 23,
             7, 2, 3, 3, 55, 20002, 20004, 20005, 20006, 16, 18, 22, 24, 25, 26]
    self.assertEqual(find_duplicates(array), [2, 3, 3, 55, 20002, 18, 22])

if __name__ == "__main__":
  unittest.main()

