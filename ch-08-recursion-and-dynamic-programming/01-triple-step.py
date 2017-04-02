# Give the number of ways to climb n steps 1, 2, or 3 steps at a time.

def triple_step(n):
  counts = [1, 1, 2, 4]
  if n < 4:
    return counts[n]
  i = 3
  while i < n:
    i += 1
    counts[i % 4] = 0
    counts[i % 4] = sum(counts)
  return counts[i % 4]

import unittest

class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(triple_step(3), 4)
    self.assertEqual(triple_step(7), 44)

if __name__ == "__main__":
  unittest.main()

