# Determine whether or not a linked list is a palindrome.

import unittest

def is_palindrome(head):
  forward, backward = head, copy_reverse(head)
  while forward:
    if forward.data != backward.data:
      return False
    forward, backward = forward.next, backward.next
  return True

def copy_reverse(head):
  prev = None
  node = copy(head)
  while node:
    next = node.next
    node.next = prev
    prev = node
    node = copy(next)
  return prev

def copy(node):
  if node:
    return Node(node.data, node.next)
  else:
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
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome(list4))
    
  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(copy_reverse(head)), "40,30,20,10")

if __name__ == "__main__":
  unittest.main()

