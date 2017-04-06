# Swap two numbers without a temporary variable.

def number_swapper(a, b):
  a ^= b
  b ^= a
  a ^= b
  return (a, b)

import unittest

class Test(unittest.TestCase):
  def test_number_swapper(self):
    a = 123456789
    b = 1010101010101010
    (a, b) = number_swapper(a, b)
    self.assertEqual(a, 1010101010101010)
    self.assertEqual(b, 123456789)

if __name__ == "__main__":
  unittest.main()

