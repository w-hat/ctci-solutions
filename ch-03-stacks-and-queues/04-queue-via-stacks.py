# Implement a queue using two stacks.

class QueueViaStacks():
  def __init__(self):
    self.in_stack = Stack()
    self.out_stack = Stack()
  
  def add(self, item):
    self.in_stack.push(item)
    
  def remove(self):
    if len(self.out_stack) == 0:
      while len(self.in_stack):
        self.out_stack.push(self.in_stack.pop())
    return self.out_stack.pop()

class Stack():
  def __init__(self):
    self.array = []
  
  def __len__(self):
    return len(self.array)
  
  def push(self, item):
    self.array.append(item)
  
  def pop(self):
    if not len(self.array):
      return None
    return self.array.pop()

import unittest

class Test(unittest.TestCase):
  def test_queue_via_stacks(self):
    queue = QueueViaStacks()
    queue.add(11)
    queue.add(22)
    queue.add(33)
    self.assertEqual(queue.remove(), 11)
    queue.add(44)
    queue.add(55)
    queue.add(66)
    self.assertEqual(queue.remove(), 22)
    self.assertEqual(queue.remove(), 33)
    self.assertEqual(queue.remove(), 44)
    self.assertEqual(queue.remove(), 55)
    queue.add(77)
    self.assertEqual(queue.remove(), 66)
    self.assertEqual(queue.remove(), 77)
    self.assertEqual(queue.remove(), None)

if __name__ == "__main__":
  unittest.main()

