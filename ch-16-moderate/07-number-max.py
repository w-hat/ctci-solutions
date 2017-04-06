# Return the larger of two numbers without any comparison operators or if
# statements.

def number_max(a, b):
  diff = b - a
  sign = (diff & (1 << 63)) >> 63
  return a * sign + b * (sign ^ 1)

import unittest

class Test(unittest.TestCase):
  def test_number_max(self):
    self.assertEqual(number_max(10000, 10), 10000)
    self.assertEqual(number_max(0x10000, 0xFFFF), 0x10000)
    self.assertEqual(number_max(1212121, 1234567), 1234567)

if __name__ == "__main__":
  unittest.main()

