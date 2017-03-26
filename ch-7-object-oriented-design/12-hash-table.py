# Implement a hash table.

class HashTable(object):
  def __init__(self, array_size=64):
    self.array = [None for _ in xrange(array_size)]
    self.count = 0
    self.capacity = 0.75 * array_size
  
  def add(self, item, value):
    if self.count >= self.capacity:
      self.expand()
    self.count += 1
    new_node = Node(item, value)
    index = hash(item) % len(self.array)
    node = self.array[index]
    if node:
      while node.next:
        node = node.next
      node.next = new_node
    else:
      self.array[index] = new_node
  
  def lookup(self, item):
    node = self.array[hash(item) % len(self.array)]
    while node:
      if node.item == item:
        return node.value
      node = node.next
    return None
  
  def delete(self, item):
    index = hash(item) % len(self.array)
    node = self.array[index]
    prev = None
    while node:
      if node.item == item:
        self.count -= 1
        if prev:
          prev.next = node.next
        else:
          self.array[index] = node.next
      prev = node
      node = node.next
  
  def expand(self):
    new_array = [None for _ in xrange(2 * len(self.array))]
    self.count = 0
    self.capacity *= 2
    self.array, prev_array = new_array, self.array
    for node in prev_array:
      while node:
        self.add(node.item, node.value)
        node = node.next
  
  def __len__(self):
    return self.count
  
class Node(object):
  def __init__(self, item, value, next=None):
    self.item, self.value, self.next = item, value, next

import unittest

class Test(unittest.TestCase):
  def test_hash_table(self):
    ht = HashTable(8)
    self.assertEqual(ht.capacity, 6)
    self.assertEqual(len(ht), 0)
    self.assertEqual(len(ht.array), 8)
    ht.add(15, "fifteen")
    ht.add(7, "seven")
    self.assertEqual(len(ht), 2)
    node_seven = ht.array[7]
    self.assertEqual(ht.array, [None,None,None,None,None,None,None,node_seven])
    self.assertEqual(node_seven.item, 15)
    self.assertEqual(node_seven.value, "fifteen")
    self.assertEqual(node_seven.next.item, 7)
    self.assertEqual(node_seven.next.value, "seven")
    self.assertEqual(node_seven.next.next, None)
    self.assertEqual(ht.lookup(15), "fifteen")
    self.assertEqual(ht.lookup(7), "seven")
    self.assertEqual(ht.lookup(24), None)
    ht.delete(24)
    ht.add(23, "twenty three")
    ht.delete(7)
    self.assertEqual(ht.lookup(7), None)
    ht.delete(15)
    self.assertEqual(ht.lookup(23), "twenty three")
    self.assertEqual(ht.lookup(15), None)
    self.assertEqual(len(ht), 1)
    ht.add(31, "thirty one")
    ht.add(15, "FIFTEEN")
    for i in xrange(70, 90):
      ht.add(i, "number " + str(i))
    self.assertEqual(len(ht), 23)
    self.assertEqual(len(ht.array), 32)
    self.assertEqual(ht.capacity, 24)
    node_fifteen = ht.array[15]
    self.assertEqual(node_fifteen.value, "FIFTEEN")
    self.assertEqual(node_fifteen.next.value, "number 79")
    self.assertEqual(ht.lookup(81), "number 81")

if __name__ == "__main__":
  unittest.main()

