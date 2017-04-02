# Implement a stack with a function that returns the current minimum item.

class MinStack():
  def __init__(self):
    self.top, self._min = None, None
    
  def min(self):
    if not self._min:
      return None
    return self._min.data
    
  def push(self, item):
    if self._min and (self._min.data < item):
      self._min = Node(data=self._min.data, next=self._min)
    else:
      self._min = Node(data=item, next=self._min)
    self.top = Node(data=item, next=self.top)
  
  def pop(self):
    if not self.top:
      return None
    self._min = self._min.next
    item = self.top.data
    self.top = self.top.next
    return item

class Node():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

import unittest

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = MinStack()
    self.assertEqual(min_stack.min(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.min(), 7)
    min_stack.push(6)
    min_stack.push(5)
    self.assertEqual(min_stack.min(), 5)
    min_stack.push(10)
    self.assertEqual(min_stack.min(), 5)
    self.assertEqual(min_stack.pop(), 10)
    self.assertEqual(min_stack.pop(), 5)
    self.assertEqual(min_stack.min(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
    self.assertEqual(min_stack.min(), None)

if __name__ == "__main__":
  unittest.main()

