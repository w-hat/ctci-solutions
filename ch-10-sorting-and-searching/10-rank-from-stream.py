# Record the number of elements lower than any given elements in a stream.

class RankNode(object):
  def __init__(self, data=None):
    self.data = data
    self.left, self.right = None, None
    if self.data is None:
      self.count = 0
    else:
      self.count = 1
    self.left_count = 0
  
  def track(self, item):
    if self.data is None:
      self.data = item
      self.count = 1
    elif self.data == item:
      self.count += 1
    elif self.data > item:
      if self.left:
        self.left.track(item)
      else:
        self.left = RankNode(item)
      self.left_count += 1
    else:
      if self.right:
        self.right.track(item)
      else:
        self.right = RankNode(item)
  
  def get_rank(self, item):
    if self.data is None:
      return 0
    elif self.data < item:
      if self.right:
        return self.count + self.left_count + self.right.get_rank(item)
      else:
        return self.count + self.left_count
    elif self.data > item:
      if self.left:
        return self.left.get_rank(item)
      else:
        return 0
    else:
      return self.left_count

import unittest

class Test(unittest.TestCase):
  def test_rank_tree(self):
    rt = RankNode()
    self.assertEqual(rt.get_rank(20), 0)
    rt.track(11)
    self.assertEqual(rt.get_rank(20), 1)
    self.assertEqual(rt.get_rank(10), 0)
    rt.track(30)
    rt.track(7)
    rt.track(7)
    rt.track(10)
    rt.track(15)
    rt.track(7)
    rt.track(3)
    rt.track(22)
    self.assertEqual(rt.get_rank(20), 7)
    self.assertEqual(rt.get_rank(7), 1)
    self.assertEqual(rt.get_rank(8), 4)
    self.assertEqual(rt.get_rank(14), 6)

if __name__ == "__main__":
  unittest.main()

