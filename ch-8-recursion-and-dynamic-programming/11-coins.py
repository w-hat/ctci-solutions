# Count the number of ways to make change for a given number of cents.

# Why settle for a slower algorithm when a constant time algorithm exists?

def coins1(cents):
  count = 0
  for c in xrange(cents, -1, -25):
    count += coins1_pnd(c)
  return count

def coins1_pnd(cents):
  count = 0
  for c in xrange(cents, -1, -10):
    count += (c / 5) + 1
  return count

def coins2(cents):
  n = cents / 5
  count  = n * n * n / 60.0
  count += n * n * 9 / 40.0
  count += n * 53 / 60.0
  count += 61 / 240.0
  return int(count + 1)

import unittest

class Test(unittest.TestCase):
  def test_coins1(self):
    self.assertEqual(coins1(0), 1)
    self.assertEqual(coins1(1), 1)
    self.assertEqual(coins1(4), 1)
    self.assertEqual(coins1(5), 2)
    self.assertEqual(coins1(15), 6)
    self.assertEqual(coins1(17), 6)
    self.assertEqual(coins1(20), 9)
    self.assertEqual(coins1(25), 13)
    self.assertEqual(coins1(52), 49)
  
  def test_coins2(self):
    for c in xrange(1000):
      self.assertEqual(coins1(c), coins2(c))
    self.assertEqual(coins2(1000000), 133342333510001)

if __name__ == "__main__":
  unittest.main()

