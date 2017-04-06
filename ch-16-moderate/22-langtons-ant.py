# -*- coding: utf-8 -*-

# Draw the grid that Langton's ant walks on after k steps.

WHITE = 0
BLACK = 1

def langtons_ant(k):
  grid = Grid()
  direction = (1, 0)
  x, y = 0, 0
  for _ in xrange(k):
    if grid.at(x, y) == WHITE:
      direction = (-direction[1], direction[0])
    else:
      direction = (direction[1], -direction[0])
    grid.flip(x, y)
    x += direction[0]
    y += direction[1]
  return str(grid)

class Grid(object):
  def __init__(self):
    self.squares = DefaultZeroDict()
    self.min_x, self.max_x = -1, 1
    self.min_y, self.max_y = -1, 1
  
  def at(self, x, y):
    return self.squares[(x, y)]
  
  def flip(self, x, y):
    self.squares[(x, y)] ^= BLACK
    self.min_x = min(self.min_x, x - 1)
    self.max_x = max(self.max_x, x + 1)
    self.min_y = min(self.min_y, y - 1)
    self.max_y = max(self.max_y, y + 1)
  
  def __str__(self):
    num_cols = 2 * (self.max_x - self.min_x) + 3
    parts = ["\n+" + "-" * num_cols + "+\n"]
    for row in xrange(self.min_y, self.max_y + 1):
      parts.append('| ')
      for col in xrange(self.min_x, self.max_x + 1):
        if self.at(col, row) == WHITE:
          parts.append("□ ")
        else:
          parts.append("■ ")
      parts.append('|\n')
    parts.append("+" + "-" * num_cols + "+\n")
    return "".join(parts)

class DefaultZeroDict(dict):
  def __missing__(self, item):
    return 0

import unittest

class Test(unittest.TestCase):
  def test_langtons_ant(self):
    string = """
+---------+
| □ □ □ □ |
| □ □ ■ □ |
| □ ■ ■ □ |
| □ □ □ □ |
+---------+"""
    self.assertEqual(langtons_ant(3).strip(), string.strip())
    string = """
+-------------+
| □ □ □ □ □ □ |
| □ ■ □ □ □ □ |
| □ ■ □ ■ □ □ |
| □ □ ■ □ ■ □ |
| □ □ □ □ ■ □ |
| □ □ ■ ■ □ □ |
| □ □ □ □ □ □ |
+-------------+"""
    self.assertEqual(langtons_ant(22).strip(), string.strip())
    string = """
+-------------------------------------+
| □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ |
| □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ □ |
| □ □ □ □ □ □ □ □ □ □ □ □ □ ■ ■ □ □ □ |
| □ □ □ □ □ □ □ □ □ □ ■ □ ■ ■ □ ■ □ □ |
| □ □ □ ■ ■ □ □ □ □ ■ ■ □ ■ □ □ ■ □ □ |
| □ □ ■ □ □ □ ■ ■ ■ ■ ■ □ ■ □ ■ □ □ □ |
| □ ■ ■ ■ □ □ □ □ □ ■ ■ □ ■ □ □ □ □ □ |
| □ ■ □ ■ □ ■ □ □ ■ ■ □ □ ■ ■ □ ■ □ □ |
| □ □ □ □ □ ■ ■ ■ □ ■ □ ■ ■ □ ■ □ ■ □ |
| □ □ □ □ □ □ ■ ■ □ ■ □ ■ □ □ □ □ ■ □ |
| □ □ □ □ ■ □ ■ □ ■ □ ■ ■ □ □ □ ■ □ □ |
| □ □ ■ □ ■ □ ■ □ ■ □ ■ □ □ □ ■ □ □ □ |
| □ ■ □ □ ■ □ ■ ■ □ □ ■ □ ■ ■ ■ □ □ □ |
| □ ■ □ ■ ■ □ ■ ■ □ □ □ ■ ■ ■ ■ ■ □ □ |
| □ □ ■ ■ □ ■ □ ■ □ □ ■ ■ ■ ■ ■ ■ □ □ |
| □ □ □ ■ ■ ■ □ □ ■ □ ■ □ ■ □ □ □ □ □ |
| □ □ □ □ □ ■ □ ■ ■ ■ □ ■ □ □ ■ □ □ □ |
| □ □ □ □ ■ □ □ □ ■ □ □ ■ □ ■ ■ □ □ □ |
| □ □ □ □ ■ □ □ □ □ □ □ □ □ ■ □ □ □ □ |
| □ □ □ □ □ ■ □ □ □ □ □ □ ■ ■ ■ □ □ □ |
| □ □ □ □ □ □ ■ ■ ■ ■ ■ ■ □ □ □ □ □ □ |
| □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ |
+-------------------------------------+
"""
    self.assertEqual(langtons_ant(1000).strip(), string.strip())

if __name__ == "__main__":
  unittest.main()

