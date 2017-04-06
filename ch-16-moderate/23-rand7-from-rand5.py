# Implement rand7 from rand5.

def rand7():
  rand14 = rand5()
  while not rand14:
    rand14 = rand5()
  if rand14 % 2:
    offset = 5
  else:
    offset = 0
  rand09 = rand5() + offset
  if rand09 < 7:
    return rand09
  else:
    return rand7()

MAPPING = {(0,0): 0, (0,1): 0, (0,2): 0, (0,3): 1, (0,4): 1, (1,0): 1,
           (1,1): 2, (1,2): 2, (1,3): 2, (1,4): 3, (2,0): 3, (2,1): 3,
           (2,2): 4, (2,3): 4, (2,4): 4, (3,0): 5, (3,1): 5, (3,2): 5,
           (3,3): 6, (3,4): 6, (4,0): 6, (4,1): 7, (4,2): 7, (4,3): 7,
           (4,4): 7}

# This version is faster.
def alt_rand7():
  pair = (rand5(), rand5())
  value = MAPPING[pair]
  if value < 7:
    return value
  else:
    return alt_rand7()

import unittest
import random

random.seed = 0

def rand5():
  return random.randint(0, 4)

class Counter(dict):
  def __missing__(self, item):
    return 0

class Test(unittest.TestCase):
  def test_rand7(self):
    talleys = Counter()
    for _ in xrange(70000):
      talleys[rand7()] += 1
    self.assertEqual(talleys[-1], 0)
    self.assertEqual(talleys[7], 0)
    for i in xrange(7):
      self.assertTrue(talleys[i] >  9000)
      self.assertTrue(talleys[i] < 11000)
  
  def test_alt_rand7(self):
    talleys = Counter()
    for _ in xrange(70000):
      talleys[alt_rand7()] += 1
    self.assertEqual(talleys[-1], 0)
    self.assertEqual(talleys[7], 0)
    for i in xrange(7):
      self.assertTrue(talleys[i] >  9000)
      self.assertTrue(talleys[i] < 11000)

if __name__ == "__main__":
  unittest.main()

