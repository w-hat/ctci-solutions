# Determine which pill bottle contains heavy pills.

def pill_bottle(bottles):
  pills = []
  for i, bottle in enumerate(bottles):
    pills += [bottle.pill()] * i
  weight = use_scale(pills)
  index = (weight - 190) * 10
  return int(index + 0.1)
  
def use_scale(pills):
  return sum(pills)

class Bottle():
  def __init__(self, pill_weight=1.0):
    self.pill_weight = pill_weight
  
  def pill(self):
    return self.pill_weight

import unittest

class Test(unittest.TestCase):
  def test_pill_bottle(self):
    bottles = [Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
               Bottle(), Bottle(), Bottle(), Bottle(), Bottle(),
               Bottle(), Bottle(), Bottle(), Bottle(), Bottle(1.1),
               Bottle(), Bottle(), Bottle(), Bottle(), Bottle()]
    self.assertEqual(pill_bottle(bottles), 14)

if __name__ == "__main__":
  unittest.main()

