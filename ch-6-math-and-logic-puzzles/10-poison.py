# Detect which of 1000 bottles contains poison using 10 detection strips.

def detect_poison(bottles, strips):
  for b, bottle in enumerate(bottles):
    for s, strip in enumerate(strips):
      if b & (1 << s):
        strip.add_drop_from(bottle)
  index = 0
  for s, strip in enumerate(strips):
    strip.wait()
    if strip.detected_poison:
      index |= (1 << s)
  return index

class Bottle():
  def __init__(self, poison):
    self.poison = poison

class Strip():
  def __init__(self):
    self.detected_poison = False
    self.drops_from = []
  
  def add_drop_from(self, bottle):
    self.drops_from.append(bottle)
  
  def wait(self):
    for drop in self.drops_from:
      if drop.poison:
        self.detected_poison = True
        return

import unittest

class Test(unittest.TestCase):
  def test_detect_posion(self):
    bottles = [Bottle(ix == 367) for ix in xrange(1000)]
    strips = [Strip() for i in xrange(10)]
    self.assertEqual(detect_poison(bottles, strips), 367)

if __name__ == "__main__":
  unittest.main()

