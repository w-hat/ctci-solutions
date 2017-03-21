# Determine what the following function does.

def is_power_of_two_or_zero(n):
  return (n & (n-1)) == 0

import unittest

class Test(unittest.TestCase):
  def test_is_power_of_two(self):
    self.assertTrue( is_power_of_two_or_zero(0))
    self.assertTrue( is_power_of_two_or_zero(1))
    self.assertTrue( is_power_of_two_or_zero(2))
    self.assertFalse(is_power_of_two_or_zero(3))
    self.assertTrue( is_power_of_two_or_zero(4))
    self.assertFalse(is_power_of_two_or_zero(5))
    self.assertFalse(is_power_of_two_or_zero(6))
    self.assertFalse(is_power_of_two_or_zero(1000))
    self.assertTrue( is_power_of_two_or_zero(1024))

if __name__ == "__main__":
  unittest.main()
