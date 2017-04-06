# Implement a least-recently-used cache.

class LRUCache(object):
  def __init__(self, capacity):
    self.items = DefaultNoneDict()
    self.ages = [None] # A min heap.
    self.time = 0
    self.capacity = capacity
  
  def add(self, key, value):
    self.ages.append((key, self.time))
    self.time += 1
    ix = len(self.ages) - 1
    self.items[key] = (value, ix)
    if ix > self.capacity:
      self.evict_one()
  
  def lookup(self, key):
    value_and_ages_ix = self.items[key]
    if value_and_ages_ix is None:
      return None
    (value, ix) = value_and_ages_ix
    self.ages[ix] = (key, self.time)
    self.bubble_down(ix)
    self.time += 1
    return value
  
  def evict_one(self):
    key = self.ages[1][0]
    del self.items[key]
    self.ages[1] = self.ages.pop()
    self.bubble_down(1)
  
  def bubble_down(self, ix):
    while 2 * ix < len(self.ages):
      next_ix = 2 * ix
      if next_ix + 1 < len(self.ages):
        if self.ages[next_ix + 1][1] < self.ages[next_ix][1]:
          next_ix += 1
      if self.ages[next_ix][1] > self.ages[ix][1]:
        break
      self.ages[ix], self.ages[next_ix] = self.ages[next_ix], self.ages[ix]
      key = self.ages[ix][0]
      (value, _) = self.items[key]
      self.items[key] = (value, ix)
      key = self.ages[next_ix][0]
      (value, _) = self.items[key]
      self.items[key] = (value, next_ix)
      ix = next_ix

class DefaultNoneDict(dict):
  def __missing__(self, item):
    return None

import unittest

class Test(unittest.TestCase):
  def test_lru_cache(self):
    cache = LRUCache(4)
    cache.add('food',  'lasagna')
    cache.add('drink', 'orange juice')
    cache.add('color', 'green')
    cache.add('dance', 'bachata')
    self.assertEqual(cache.ages,
        [None, ('food', 0), ('drink', 1), ('color', 2), ('dance', 3)])
    cache.add('sport', 'ultimate')
    self.assertEqual(cache.ages,
        [None, ('drink', 1), ('dance', 3), ('color', 2), ('sport', 4)])
    self.assertEqual(cache.lookup('dance'), 'bachata')
    self.assertEqual(cache.ages,
        [None, ('drink', 1), ('sport', 4), ('color', 2), ('dance', 5)])
    self.assertEqual(cache.lookup('food'), None)
    cache.add('spice', 'paprika')
    self.assertEqual(cache.ages,
        [None, ('color', 2), ('sport', 4), ('spice', 6), ('dance', 5)])
    self.assertEqual(cache.lookup('drink'), None)
    self.assertEqual(cache.lookup('color'), 'green')
    self.assertEqual(cache.ages,
        [None, ('sport', 4), ('dance', 5), ('spice', 6), ('color', 7)])

if __name__ == "__main__":
  unittest.main()

