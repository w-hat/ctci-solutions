# Return an array of linked lists containing all elements on each depth
# of a binary tree.

def list_of_depths(binary_tree):
  if not binary_tree:
    return []
  lists = []
  queue = Queue()
  current_depth = -1
  current_tail = None
  node = binary_tree
  node.depth = 0
  while node:
    if node.depth == current_depth:
      current_tail.next = ListNode(node.data)
      current_tail = current_tail.next
    else:
      current_depth = node.depth
      current_tail = ListNode(node.data)
      lists.append(current_tail)
    for child in [node.left, node.right]:
      if child:
        child.depth = node.depth + 1
        queue.add(child)
    node = queue.remove()
  return lists

class TreeNode():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
    self.depth = None

class ListNode():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    return str(self.data) + ',' + str(self.next)

class Queue():
  def __init__(self):
    self.head, self.tail = None, None
  
  def add(self, item):
    if self.head:
      self.tail.next = ListNode(item)
      self.tail = self.tail.next
    else:
      self.head = self.tail = ListNode(item)
  
  def remove(self):
    if not self.head:
      return None
    item = self.head.data
    self.head = self.head.next
    return item

import unittest

class Test(unittest.TestCase):
  def test_list_of_depths(self):
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lists = list_of_depths(node_a)
    self.assertEqual(str(lists[0]), "A,None")
    self.assertEqual(str(lists[1]), "B,C,None")
    self.assertEqual(str(lists[2]), "D,E,F,None")
    self.assertEqual(str(lists[3]), "H,G,None")
    self.assertEqual(len(lists), 4)

if __name__ == "__main__":
  unittest.main()

