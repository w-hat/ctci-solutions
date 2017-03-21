# Insert `m` into `n` between `i` and `j`.

def insertion(n, m, i, j):
  cleared_n = n & ~((1 << (j+1)) - (1 << i))
  shifted_m = m << i
  return cleared_n | shifted_m 

import unittest

class Test(unittest.TestCase):
  def test_insertion(self):
    self.assertEqual(insertion(0b11111111, 0b10, 2, 5), 0b11001011)
    self.assertEqual(insertion(0b00000000, 0b1010, 4, 7), 0b10100000)

if __name__ == "__main__":
  unittest.main()

