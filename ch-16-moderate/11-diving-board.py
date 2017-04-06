# How many lengths can the diving board be?

def diving_board(k, shorter, longer):
  if shorter == longer:
    return [k * shorter]
  return range(k * shorter, k * longer + 1, longer - shorter)

import unittest

class Test(unittest.TestCase):
  def test_diving_board(self):
    self.assertEqual(diving_board(5, 3, 4), [15, 16, 17, 18, 19, 20])
    self.assertEqual(diving_board(4, 2, 6), [8, 12, 16, 20, 24])

if __name__ == "__main__":
  unittest.main()

