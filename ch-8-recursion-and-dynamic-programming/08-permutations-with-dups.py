# List all permutation of the letters in the given string.

def permutations(string):
  return partial_permutations("", sorted(string))

def partial_permutations(partial, letters):
  if len(letters) == 0:
    return [partial]
  permutations = []
  previous_letter = None
  for i, letter in enumerate(letters):
    if letter == previous_letter:
      continue
    next_partial = partial + letter
    next_letters = letters[:i] + letters[(i+1):]
    permutations += partial_permutations(next_partial, next_letters)
    previous_letter = letter
  return permutations

import unittest

class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutations("abca"), ["aabc", "aacb", "abac", "abca",
        "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])
    self.assertEqual(permutations("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])

if __name__ == "__main__":
  unittest.main()

