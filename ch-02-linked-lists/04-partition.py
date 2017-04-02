# Partition a linked list so that all of the nodes containing values less than
# a pivot value occur before all of the nodes containing values greater than
# or equal to the pivot value.

import unittest

def partition(head, pivot):
  a_head, a_tail = None, None
  b_head, b_tail = None, None
  node = head
  while node:
    if node.data < pivot:
      if a_head:
        a_tail.next, a_tail = node, node
      else:
        a_head, a_tail = node, node
    else:
      if b_head:
        b_tail.next, b_tail = node, node
      else:
        b_head, b_tail = node, node
    node = node.next
  a_tail.next = b_head
  return a_head

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_partition(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition(head1, 6)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = partition(head2, 7)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")

if __name__ == "__main__":
  unittest.main()

