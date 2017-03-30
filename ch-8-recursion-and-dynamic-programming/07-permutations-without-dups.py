# List all permutations of a string that contains no duplicate letters.

def permutations(string):
  return partial_permutations("", string)

def partial_permutations(partial, letters_left):
  if len(letters_left) == 0:
    return [partial]
  permutations = []
  for i, letter in enumerate(letters_left):
    next_letters_left = letters_left[:i] + letters_left[(i+1):]
    permutations += partial_permutations(partial + letter, next_letters_left)
  return permutations

import unittest

class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutations("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])

if __name__ == "__main__":
  unittest.main()

