# Determine a build order given a list of projects and their dependencies.

def build_order(projects, dependencies):
  nodes = {}
  for project in projects:
    nodes[project] = GraphNode(project)
  for dependency in dependencies:
    nodes[dependency[0]].add_edge(nodes[dependency[1]])
  queue = Queue()
  for project in projects:
    node = nodes[project]
    if not node.dependencies_left:
      queue.add(node)
  build_order = []
  while queue.is_not_empty():
    node = queue.remove()
    build_order.append(node.data)
    for dependent in node.edges:
      dependent.dependencies_left -= 1
      if not dependent.dependencies_left:
        queue.add(dependent)
  if len(build_order) < len(projects):
    return Exception("Cycle detected")
  return build_order

class GraphNode():
  def __init__(self, data):
    self.data = data
    self.edges = []
    self.dependencies_left = 0
    
  def add_edge(self, node):
    self.edges.append(node)
    node.dependencies_left += 1

class Queue():
  def __init__(self):     self.array = []
  def add(self, item):    self.array.append(item)
  def remove(self):       return self.array.pop(0)
  def is_not_empty(self): return len(self.array) > 0

import unittest

class Test(unittest.TestCase):
  def test_build_order(self):
    projects = ["A", "B", "C", "D", "E", "F", "G"]
    dependencies1 = [("C", "A"), ("B", "A"), ("F", "A"), ("F", "B"), ("F", "C"),
        ("A", "E"), ("B", "E"), ("D", "G")]
    self.assertEqual(build_order(projects, dependencies1),
        ["D", "F", "G", "B", "C", "A", "E"])
    dependencies2 = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
    self.assertEqual(build_order(projects, dependencies2).__class__, Exception)
    dependencies3 = [("A", "B"), ("A", "C"), ("E", "A"), ("E", "B"), ("A", "F"),
        ("B", "F"), ("C", "F"), ("G", "D")]
    self.assertEqual(build_order(projects, dependencies3),
        ["E", "G", "A", "D", "B", "C", "F"])

if __name__ == "__main__":
  unittest.main()

