# Add two numbers without using +.

import ctypes

def add_without_plus(a, b):
  both_bits = a & b
  single_bits = a ^ b
  if both_bits == 0:
    return single_bits
  carry_bits = (both_bits << 1) & 0x1FFFFFFFFFFFFFFFF
  if carry_bits & (1 << 64):
    return ctypes.c_long(single_bits).value
  return add_without_plus(single_bits, carry_bits)

import unittest

class Test(unittest.TestCase):
  def test_add_without_plus(self):
    self.assertEqual(add_without_plus(1, 1), 2)
    self.assertEqual(add_without_plus(1, 2), 3)
    self.assertEqual(add_without_plus(1001, 234), 1235)
    self.assertEqual(add_without_plus(5, -1), 4)
    self.assertEqual(add_without_plus(7,-5), 2)
    self.assertEqual(add_without_plus(7,-29), -22)
    self.assertEqual(add_without_plus(-2,10), 8)

if __name__ == "__main__":
  unittest.main()

