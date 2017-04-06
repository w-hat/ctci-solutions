# Find the best fit line to the points.

def best_line(points):
  average_x = float(sum([p.x for p in points]))/len(points)
  average_y = float(sum([p.y for p in points]))/len(points)
  shifted_points = [Point(p.x - average_x, p.y - average_x) for p in points]
  slope = best_slope_through_origin(shifted_points)
  intercept = average_y - slope * average_x
  if not slope:
    return None
  return lambda x: slope * x + intercept

def best_slope_through_origin(points):
  denominator = sum([p.x * p.x for p in points])
  if denominator == 0:
    return None
  numerator = sum([p.x * p.y for p in points])
  return float(numerator) / denominator

class Point(object):
  def __init__(self, x, y):
    self.x, self.y = x, y

import unittest

class Test(unittest.TestCase):
  def test_best_line(self):
    points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4)]
    line = best_line(points)
    self.assertEqual(line(0), 0)
    self.assertEqual(line(1.5), 1.5)
    self.assertEqual(line(10.3), 10.3)
    line = best_line([Point(p.x + 0.125, p.y + 5.4) for p in points])
    self.assertEqual(line(0), 5.275)
    self.assertEqual(line(9), 14.275)
    points = [Point(1, 2), Point(2, 1), Point(3, 4), Point(4, 5), Point(5, 6)]
    line = best_line(points)
    self.assertAlmostEqual(line(1), 1.2, 14)
    self.assertEqual(line(5), 6)
    points[-1].y = 7
    self.assertAlmostEqual(line(2), 2.4, 14)

if __name__ == "__main__":
  unittest.main()

