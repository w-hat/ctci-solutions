# Determine whether one binary tree is a subtree of another.

def is_subtree(bt1, bt2):
  for node in tree_generator(bt1):
    if equivalent_trees(node, bt2):
      return True
  return False

def equivalent_trees(bt1, bt2):
  if not bt1:
    return not bt2
  if not bt2:
    return False
  if bt1.data != bt2.data:
    return False
  return equivalent_trees(bt1.left, bt2.left) and \
         equivalent_trees(bt1.right, bt2.right)

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    
def tree_generator(node):
  if not node: return
  yield node
  for child in tree_generator(node.left):  yield child
  for child in tree_generator(node.right): yield child

import unittest

class Test(unittest.TestCase):
  def test_is_subtree(self):
    tree1 = Node(5,Node(3,Node(2),Node(4)),Node(8,Node(7,Node(9)),Node(1)))
    tree2 = Node(8,Node(7),Node(1))
    self.assertEqual(is_subtree(tree1, tree2), False)
    tree3 = Node(8,Node(7,Node(9)),Node(1))
    self.assertEqual(is_subtree(tree1, tree3), True)

if __name__ == "__main__":
  unittest.main()

