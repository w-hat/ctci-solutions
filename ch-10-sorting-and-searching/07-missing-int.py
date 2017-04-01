# Find an integer that is not contained in a list of 4 billion integers.

import random

def missing_int(integer_list):
  guess = random.randint(0, (1 << 64) - 1)
  for integer in integer_list:
    if integer == guess:
      return missing_int(integer_list)
  return guess

import unittest

class Test(unittest.TestCase):
  def test_missing_int(self):
    integer_list = [400, 438, 998098093, 171, 10003]
    integer = missing_int(integer_list)
    self.assertFalse( integer in integer_list)

if __name__ == "__main__":
  unittest.main()

