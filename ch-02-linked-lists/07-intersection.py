# Return an intersecting node if two linked lists intersect.

import unittest


def get_size_and_tail(head):
  if not head:
    return None

  counter = 1
  node = head
  while node.next:
    counter += 1
    node = node.next

  return (counter, node)

# n - size of head1 list, m - size of head2 list
# run in O(n+m) time and in O(1) space
def intersection_witout_storage(head1, head2):
  size1, tail1 = get_size_and_tail(head1)
  size2, tail2 = get_size_and_tail(head2)

  # if the tails are different there is no intersection
  if tail1 != tail2:
    return None

  if size1 > size2:
    longer, shorter = head1, head2
  else:
    longer, shorter = head2, head1

  # skipping the first (extra) nodes from the begining of the longer list
  for _ in range(abs(size1 - size2)):
    if longer and longer.next:
      longer = longer.next


  while longer != shorter:
    longer = longer.next
    shorter = shorter.next

  return longer


# n - size of head1 list, m - size of head2 list
# run in O(n+m) time and in O(n+m) space - more elegance
def intersection(head1, head2):
  nodes = {}
  node = head1
  while node:
    nodes[node] = True
    node = node.next
  node = head2
  while node:
    if node in nodes:
      return node
    node = node.next
  return None

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection(head1, head2), None)
    self.assertEqual(intersection_witout_storage(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection(head3, head4), node)
    self.assertEqual(intersection_witout_storage(head3, head4), node)

  def test_get_size_and_tail(self):
    tail = Node(30)
    head1 = Node(10, Node(20, tail))
    self.assertEquals(get_size_and_tail(head1), (3, tail))

if __name__ == "__main__":
  unittest.main()

