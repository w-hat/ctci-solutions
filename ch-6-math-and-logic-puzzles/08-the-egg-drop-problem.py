# What is the best floor to drop an egg from in an n-story building if you
# have k eggs left if you want to determine the highest floor from which an 
# egg can fall without breaking while minimizing the number of drops you
# must perform.  Assume a uniform distribution of breaking floors.
# Note that this differs slightly from the book's problem in that we want to
# minimize *average* drops rather than the worst case scenario.

def egg_drop_floor(n, k):
  if k == 0:
    return (None, None)
  if k == 1:
    return (1, float(n+1)/2.0)
  # Allocate a table to store the average drops given a number of floors and a 
  # number of eggs.
  table = [[0.0 for i in xrange(k+1)] for j in xrange(n+1)]
  # If we only have one egg left, we need drop from one level higher each time.
  for floor in xrange(1, n+1):
    table[floor][1] = float(floor+1)/2.0
  # Given a number of floors and a number of eggs, consider what happens
  # if the egg breaks and if it does not break.
  best_floor = n + 1
  for eggs_left in xrange(2, k+1):
    table[1][eggs_left] = 1.0
    for floor in xrange(2, n+1):
      minimum_average_drops = n + 1
      for drop_floor in xrange(1, floor+1):
        egg_breaks = float(drop_floor)/float(floor)
        average_drops = 1.0
        average_drops += egg_breaks*table[drop_floor][eggs_left - 1]
        average_drops += (1 - egg_breaks)*table[floor - drop_floor][eggs_left]
        if average_drops < minimum_average_drops:
          minimum_average_drops = average_drops
          best_floor = drop_floor
      table[floor][eggs_left] = minimum_average_drops
  return (best_floor, table[n][k])

import unittest

class Test(unittest.TestCase):
  def test_egg_drop_floor(self):
    (start_floor, best_average_drops) = egg_drop_floor(100, 1)
    self.assertEqual(start_floor, 1)
    self.assertEqual(best_average_drops, 50.5)
    (start_floor, best_average_drops) = egg_drop_floor(128, 8)
    self.assertEqual(start_floor, 64)
    self.assertAlmostEqual(best_average_drops, 8.0, 1)
    # The assertions below were not verified as correct.
    (start_floor, best_average_drops) = egg_drop_floor(100, 2)
    self.assertEqual(start_floor, 13)
    self.assertAlmostEqual(best_average_drops, 10.4, 1)
    (start_floor, best_average_drops) = egg_drop_floor(100, 3)
    self.assertEqual(start_floor, 28)
    self.assertAlmostEqual(best_average_drops, 7.8, 1)

if __name__ == "__main__":
  unittest.main()

