# Count the number of zeros at the end of a factorial.

def factorial_zeros(n):
  five_factors = 0
  while n > 4:
    n /= 5
    five_factors += n
  return five_factors

import unittest

class Test(unittest.TestCase):
  def test_factorial_zeros(self):
    self.assertEqual(factorial_zeros(4), 0)
    self.assertEqual(factorial_zeros(9), 1)
    self.assertEqual(factorial_zeros(10), 2)
    self.assertEqual(factorial_zeros(25), 6)
    self.assertEqual(factorial_zeros(55), 13)

if __name__ == "__main__":
  unittest.main()

