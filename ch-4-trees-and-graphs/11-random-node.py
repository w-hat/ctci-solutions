# Design a binary tree class that can return a random node.

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.count = 1
    if self.left:
      self.count += self.left.count
    if self.right:
      self.count += self.right.count

  def get_random_node(self):
    return self.get_numbered_node(randint(0, self.count - 1))

  def get_numbered_node(self, number):
    if number == 0:
      return self
    if self.left:
      if number - 1 < self.left.count:
        return self.left.get_numbered_node(number - 1)
      elif self.right:
        return self.right.get_numbered_node(number - 1 - self.left.count)
    if self.right:
      return self.right.get_numbered_node(number - 1)
    return None

import random
import unittest

mock_random_value = False

def randint(lower_bound, upper_bound):
  if not mock_random_value is False:
    return mock_random_value
  return random.randint(lower_bound, upper_bound)

class Test(unittest.TestCase):
  def test_mock_randint(self):
    global mock_random_value
    mock_random_value = 12
    self.assertEqual(randint(0, 2000), 12)
  
  def test_get_random_value(self):
    global mock_random_value
    tree = Node(11,Node(21,Node(31),Node(32,Node(41),Node(42,None,Node(51)))),
                   Node(22,Node(33),Node(34)))
    mock_random_value = 0
    self.assertEqual(tree.get_random_node().data, 11)
    mock_random_value = 4
    self.assertEqual(tree.get_random_node().data, 41)
    mock_random_value = 8
    self.assertEqual(tree.get_random_node().data, 33)

if __name__ == "__main__":
  unittest.main()

