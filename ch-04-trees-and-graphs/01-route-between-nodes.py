# Find a route from the first node to the second node in a directed graph.

def find_route(node1, node2):
  found_path = None
  queue = Queue()
  node = node1
  node.shortest_path = [node]
  all_visited_nodes = [node]
  while node:
    for adjacent in node.adjacency_list:
      if not adjacent.shortest_path:
        adjacent.shortest_path = node.shortest_path + [adjacent]
        if adjacent == node2:
          found_path = node.shortest_path + [adjacent]
          break
        queue.add(adjacent)
        all_visited_nodes.append(adjacent)
    node = queue.remove()
  for visited in all_visited_nodes:
    visited.shortest_path = None
  return found_path
  
class Node():
  def __init__(self, data, adjacency_list=None):
    self.data = data
    self.adjacency_list = adjacency_list or []
    self.shortest_path = None
  
  def add_edge_to(self, node):
    self.adjacency_list += [node]

  def __str__(self):
    return self.data

class Queue():
  def __init__(self):
    self.array = []
  
  def add(self, item):
    self.array.append(item)
  
  def remove(self):
    if not len(self.array):
      return None
    item = self.array[0]
    del self.array[0]
    return item

import unittest

def str_for(path):
  if not path: return str(path)
  return ''.join([str(n) for n in path])

class Test(unittest.TestCase):
  def test_find_route(self):
    node_j = Node('J')
    node_i = Node('I')
    node_h = Node('H')
    node_d = Node('D')
    node_f = Node('F', [node_i])
    node_b = Node('B', [node_j])
    node_g = Node('G', [node_d, node_h])
    node_c = Node('C', [node_g])
    node_a = Node('A', [node_b, node_c, node_d])
    node_e = Node('E', [node_f, node_a])
    node_d.add_edge_to(node_a)
    self.assertEqual(str_for(find_route(node_a, node_i)), 'None')
    self.assertEqual(str_for(find_route(node_a, node_j)), 'ABJ')
    node_h.add_edge_to(node_i)
    self.assertEqual(str_for(find_route(node_a, node_i)), 'ACGHI')

if __name__ == "__main__":
  unittest.main()

