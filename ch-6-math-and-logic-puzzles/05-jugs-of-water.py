# Measure 4 liters with a 5 liter jug and a 3 liter jug.

def measure_four():
  jug3 = Jug(3)
  jug5 = Jug(5)
  jug3.fill()
  jug3.pour(jug5)
  jug3.fill()
  jug3.pour(jug5)
  jug5.dump()
  jug3.pour(jug5)
  jug3.fill()
  jug3.pour(jug5)
  return jug5.water

class Jug():
  def __init__(self, capacity):
    self.capacity = capacity
    self.water = 0
  
  def fill(self):
    self.water = self.capacity
  
  def pour(self, jug):
    total = self.water + jug.water
    jug.water = min(jug.capacity, total)
    self.water = total - jug.water
  
  def dump(self):
    self.water = 0

import unittest

class Test(unittest.TestCase):
  def test_measure_four(self):
    self.assertEqual(measure_four(), 4)

if __name__ == "__main__":
  unittest.main()

