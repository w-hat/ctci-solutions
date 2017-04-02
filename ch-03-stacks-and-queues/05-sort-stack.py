# Sort a stack with the smallest on top using only a single temporary stack.

def sort_stack(stack):
  temp = Stack()
  previous = stack.pop()
  current = stack.pop()
  while current:
    if current < previous:
      temp.push(current)
    else:
      temp.push(previous)
      previous = current
    current = stack.pop()
  is_sorted = True
  current = temp.pop()
  while current:
    if current > previous:
      is_sorted = False
      stack.push(current)
    else:
      stack.push(previous)
      previous = current
    current = temp.pop()
  stack.push(previous)
  if is_sorted:
    return stack
  return sort_stack(stack)

class Stack():
  def __init__(self):
    self.top = None
  
  def __str__(self):
    return str(self.top)
  
  def push(self, item):
    self.top = current(item, self.top)
  
  def pop(self):
    if not self.top:
      return None
    item = self.top
    self.top = self.top.next
    return item.data

class current():
  def __init__(self, data=None, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    return str(self and self.data) + ',' + str(self and self.next)

import unittest

class Test(unittest.TestCase):
  def test_sort_stack(self):
    self.assertEqual(str(sort_stack(Stack())), "None,None")
    stack = Stack()
    stack.push(10)
    stack.push(30)
    stack.push(70)
    stack.push(40)
    stack.push(80)
    stack.push(20)
    stack.push(90)
    stack.push(50)
    stack.push(60)
    self.assertEqual(str(stack), "60,50,90,20,80,40,70,30,10,None")
    self.assertEqual(str(sort_stack(stack)), "10,20,30,40,50,60,70,80,90,None")

if __name__ == "__main__":
  unittest.main()

