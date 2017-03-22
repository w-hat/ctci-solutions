# How likely is it that ants on a polygon will run into each other if they
# walk at constant speed but start in a random direction.

def ants_on_a_polygon(n):
  return 1 - 0.5 ** (n - 1)

import unittest

class Test(unittest.TestCase):
  def test_ants_on_a_polygon(self):
    self.assertEqual(ants_on_a_polygon(3), 0.75)
    self.assertEqual(ants_on_a_polygon(4), 0.875)

if __name__ == "__main__":
  unittest.main()

