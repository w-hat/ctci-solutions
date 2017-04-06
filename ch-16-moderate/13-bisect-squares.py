# Bisect the squares.

def bisect_squares(square1, square2):
  center1, center2 = square1.center, square2.center
  xdiff = center2.x - center1.x
  ydiff = center2.y - center1.y
  if xdiff == 0:
    if ydiff == 0:
      return lambda x: center1.y
    else:
      # Vertical line.
      return None
  slope = float(ydiff) / xdiff
  intercept = center1.y - center1.x * slope
  return lambda x: slope * x + intercept

class Square(object):
  def __init__(self, center, side_length, rotation):
    self.center, self.side_length, self.rotation = center, side_length, rotation

class Point(object):
  def __init__(self, x, y):
    self.x, self.y = x, y

import unittest
import random

class Test(unittest.TestCase):
  def test_bisect_squares(self):
    sq1 = Square(Point(2, 4.5), 2, 15)
    sq2 = Square(Point(7, 4.5), 3, 45)
    line = bisect_squares(sq1, sq2)
    self.assertEqual(line(0), 4.5)
    self.assertEqual(line(11), 4.5)
    for _ in xrange(10):
      center1 = Point(random.uniform(-10, 10), random.uniform(-10, 10))
      center2 = Point(random.uniform(-10, 10), random.uniform(-10, 10))
      square1 = Square(center1, random.uniform(1, 9), random.uniform(0, 90))
      square2 = Square(center2, random.uniform(1, 9), random.uniform(0, 90))
      line = bisect_squares(square1, square2)
      self.assertAlmostEqual(line(center1.x), center1.y, 7)
      self.assertAlmostEqual(line(center2.x), center2.y, 7)
      mid_x = (center1.x + center2.x) / 2
      mid_y = (center1.y + center2.y) / 2
      self.assertAlmostEqual(line(mid_x), mid_y, 7)

if __name__ == "__main__":
  unittest.main()

