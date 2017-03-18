# Validate that a binary tree is a binary search tree.

def validate_tree(binary_tree):
  return validate_tree_node(binary_tree, -float('inf'), float('inf'))

def validate_tree_node(node, left_bound, right_bound):
  if not node:
    return True
  return node.data >= left_bound and node.data <= right_bound and \
         validate_tree_node(node.left, left_bound, node.data) and \
         validate_tree_node(node.right, node.data, right_bound)

class Node():
  def __init__(self, data, left=None, right=None):
    self.data, self.left, self.right = data, left, right

import unittest

class Test(unittest.TestCase):
  def test_validate_tree(self):
    self.assertEqual(validate_tree(Node(3,Node(1),Node(8))), True)
    tree1 = Node(5,Node(3,Node(1),Node(4)),Node(7,Node(6),Node(8,None,Node(9))))
    self.assertEqual(validate_tree(tree1), True)
    tree2 = Node(7,Node(3,Node(1),Node(8)),Node(9,Node(8),Node(11)))
    self.assertEqual(validate_tree(tree2), False)

if __name__ == "__main__":
  unittest.main()

