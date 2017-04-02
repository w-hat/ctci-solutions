# Tell how many bits must be flipped in order to transform one number into 
# the other.

EVEN = 0x5555555555555555
ODD  = 0xAAAAAAAAAAAAAAAA

# This is better for numbers that are nearly the same.
def bits_different_1(a, b):
  different = a ^ b
  count = 0
  while different:
    different ^= different & -different
    count += 1
  return count

# This is better for numbers that differ by a lot.
def bits_different_2(a, b):
  different = a ^ b
  counts = (different & EVEN) + ((different & ODD) >> 1)
  counts = (counts & 0x3333333333333333) + ((counts & 0xCCCCCCCCCCCCCCCC) >> 2)
  counts = (counts & 0x0F0F0F0F0F0F0F0F) + ((counts & 0xF0F0F0F0F0F0F0F0) >> 4)
  counts = (counts & 0x00FF00FF00FF00FF) + ((counts & 0xFF00FF00FF00FF00) >> 8)
  counts = (counts & 0x0000FFFF0000FFFF) + ((counts & 0xFFFF0000FFFF0000) >> 16)
  counts = (counts & 0x00000000FFFFFFFF) + (counts >> 32)
  return counts

import unittest

class Test(unittest.TestCase):
  def test_bits_different_1(self):
    self.assertEqual(bits_different_1(16, 2), 2)
    self.assertEqual(bits_different_1(17, 34), 4)
    self.assertEqual(bits_different_1(15, 97), 5)
  
  def test_bits_different_2(self):
    self.assertEqual(bits_different_2(16, 2), 2)
    self.assertEqual(bits_different_2(17, 34), 4)
    self.assertEqual(bits_different_2(15, 97), 5)

if __name__ == "__main__":
  unittest.main()

