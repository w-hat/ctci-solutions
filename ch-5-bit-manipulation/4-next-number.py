# Return the next larger and next smaller numbers that use the same number of 
# 1's in their binary representation as the given positive integer.

def next_numbers(number):
  if number % 2:
    # Larger X011...1 --> X101...1
    negated = ~number
    lsz = negated & -negated
    larger = number ^ (lsz | (lsz >> 1))
    # Smaller X100...01...1 --> X011...10...0
    end_ones = lsz - 1
    cleared = number ^ end_ones
    if cleared:
      next_bit = cleared & -cleared
      flip_bits1 = next_bit | (next_bit >> 1)
      extra_zeros = ((next_bit >> 1) - 1) ^ end_ones
      flip_bits2 = extra_zeros | (extra_zeros >> end_ones.bit_length())
      smaller = number ^ flip_bits1 ^ flip_bits2
    else:
      smaller = None
  else:
    # Smaller X100...0 --> X010...0
    lsb = number & -number
    smaller = number ^ (lsb | (lsb >> 1))
    # Larger X011...10...0 --> X100...01...1
    end_zeros = lsb - 1
    cleared_negated = ~number ^ end_zeros
    next_zero = cleared_negated & -cleared_negated
    flip_bits1 = next_zero | (next_zero >> 1)
    extra_ones = ((next_zero >> 1) - 1) ^ end_zeros
    flip_bits2 = extra_ones | (extra_ones >> end_zeros.bit_length())
    larger = number ^ flip_bits1 ^ flip_bits2
  return (smaller, larger)

import unittest

class Test(unittest.TestCase):
  def test_next_numbers(self):
    self.assertEqual(next_numbers(8), (4, 16))
    self.assertEqual(next_numbers(12), (10, 17))
    self.assertEqual(next_numbers(15), (None, 23))
    self.assertEqual(next_numbers(143), (124, 151))
    self.assertEqual(next_numbers(159), (126, 175))

if __name__ == "__main__":
  unittest.main()

