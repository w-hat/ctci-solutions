# Design an efficient circular array.

class CircularArray(object):
  def __init__(self, array):
    self.array = array
    self.start = 0
  
  def rotate(self, i):
    self.start = (self.start + i) % len(self.array)
  
  def __iter__(self):
    for i in xrange(self.start, len(self.array)):
      yield self.array[i]
    for i in xrange(0, self.start):
      yield self.array[i]
  
  def __getitem__(self, i):
    return self.array[(self.start + i) % len(self.array)]
    
  def __setitem__(self, i, item):
    self.array[(self.start + i) % len(self.array)] = item
  
  def __delitem__(self, i):
    index = (self.start + i) % len(self.array)
    del self.array[index]
    if index < self.start:
      self.start -= 1

import unittest

class Test(unittest.TestCase):
  def test_circular_array(self):
    ca = CircularArray([11, 22, 33, 44, 55, 66, 77])
    ca.rotate(5)
    self.assertEqual(ca[0], 66)
    array = []
    for item in ca:
      array.append(item)
    self.assertEqual(array, [66, 77, 11, 22, 33, 44, 55])
    ca[3] = 999
    del ca[4]
    array = []
    for item in ca:
      array.append(item)
    self.assertEqual(array, [66, 77, 11, 999, 44, 55])
    ca.rotate(2)
    array = []
    for item in ca:
      array.append(item)
    self.assertEqual(array, [11, 999, 44, 55, 66, 77])

if __name__ == "__main__":
  unittest.main()

