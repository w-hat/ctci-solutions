# Choose a subset randomly in Java.

# Build the Java .class file with `ant`.

import RandoSet

def random_subset(array, seed):
  rando = RandoSet(array, seed)
  subset = rando.randomSubset()
  return subset

import unittest

class Test(unittest.TestCase):
  def test_random_subset(self):
    array = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    subset = [str(x) for x in random_subset(array, 12)]
    self.assertEqual(subset, ["one", "seven", "eight"])

if __name__ == "__main__":
  unittest.main()

