# Return a binary string representation of the given floating point number
# between 0 and 1 as long as it accurately fits in 32 bits.

import ctypes

def binary_to_string(number):
  if number == 1:
    return "1.0"
  if number == 0:
    return "0.0"
  if number < 0 or number > 1:
    return Exception("Out of bounds")
  normalized = bits_for(number + 1.0)
  bits = normalized & ((1 << 52) - 1)
  if normalized & ((1 << 22) - 1):
    return Exception("Insufficient precision")
  digits = ["0."]
  bit = (1 << 51)
  while bits:
    if bits & bit:
      digits.append("1")
    else:
      digits.append("0")
    bits &= ~bit
    bit >>= 1
  return "".join(digits)

def bits_for(number):
  return ctypes.c_longlong.from_buffer(ctypes.c_double(number)).value

import unittest

class Test(unittest.TestCase):
  def test_binary_to_string(self):
    self.assertEqual(binary_to_string(0.75), "0.11")
    self.assertEqual(binary_to_string(0.625), "0.101")
    self.assertEqual(binary_to_string(0.3).message, "Insufficient precision")

if __name__ == "__main__":
  unittest.main()

