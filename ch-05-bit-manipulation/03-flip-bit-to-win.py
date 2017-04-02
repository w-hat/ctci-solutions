# Determine the longest sequence of 1s attainable by flipping up to one digit.

def longest_sequence_after_flip(bits):
  bit = 1 << 63
  longest = 0
  current_without_flip = 0
  current_with_flip = 0
  while bit:
    if bits & bit:
      current_without_flip += 1
      current_with_flip += 1
    else:
      current_with_flip = current_without_flip + 1
      current_without_flip = 0
    if current_with_flip > longest:
      longest = current_with_flip
    bit >>= 1
  return longest

import unittest

class Test(unittest.TestCase):
  def test_longest_sequence_after_flip(self):
    self.assertEqual(longest_sequence_after_flip(0b1111100), 6)
    self.assertEqual(longest_sequence_after_flip(0b0111111), 7)
    self.assertEqual(longest_sequence_after_flip(-1), 64)
    self.assertEqual(longest_sequence_after_flip(0b1011110111001111110), 8)

if __name__ == "__main__":
  unittest.main()

