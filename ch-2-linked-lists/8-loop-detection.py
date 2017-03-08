# Detect whether or not a linked list contains a cycle.

import unittest

def detect_cycle(head):
  nodes = {}
  node = head
  while node:
    if node in nodes:
      return node
    nodes[node] = True
    node = node.next
  return None

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_detect_cycle(self):
    head1 = Node(100,Node(200,Node(300)))
    self.assertEqual(detect_cycle(head1), None)
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    self.assertEqual(detect_cycle(head2), node1)

if __name__ == "__main__":
  unittest.main()
