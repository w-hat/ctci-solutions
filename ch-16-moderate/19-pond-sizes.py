# Determine the sizes of the ponds.

def pond_sizes(terrain):
  if len(terrain) == 0 or len(terrain[0]) == 0:
    return []
  sizes = set()
  n, m = len(terrain), len(terrain[0])
  visited = [[False] * m for _ in xrange(n)]
  for r in xrange(n):
    for c in xrange(m):
      if not terrain[r][c] and not visited[r][c]:
        sizes.add(pond_size(terrain, visited, r, c))
  return sizes

def pond_size(terrain, visited, row, col):
  if terrain[row][col] or visited[row][col]:
    return 0
  visited[row][col] = True
  size = 1
  if row > 0:
    size +=   pond_size(terrain, visited, row - 1, col)
    if col > 0:
      size += pond_size(terrain, visited, row - 1, col - 1)
    if col < len(terrain[0]) - 1:
      size += pond_size(terrain, visited, row - 1, col + 1)
  if row < len(terrain) - 1:
    size +=   pond_size(terrain, visited, row + 1, col)
    if col > 0:
      size += pond_size(terrain, visited, row + 1, col - 1)
    if col < len(terrain[0]) - 1:
      size += pond_size(terrain, visited, row + 1, col + 1)
  if col > 0:
    size +=   pond_size(terrain, visited, row, col - 1)
  if col < len(terrain[0]) - 1:
    size +=   pond_size(terrain, visited, row, col + 1)
  return size

import unittest

class Test(unittest.TestCase):
  def test_pond_sizes(self):
    terrain = [[0, 0, 1, 2, 3, 1, 1, 1],
               [1, 1, 1, 2, 2, 2, 0, 1],
               [1, 0, 1, 1, 2, 1, 1, 2],
               [0, 1, 0, 1, 3, 1, 2, 3]]
    self.assertEqual(pond_sizes(terrain), {1, 2, 3})
    terrain = [[0, 0, 1, 2, 3, 1, 0, 1, 1],
               [0, 1, 1, 2, 2, 2, 0, 0, 1],
               [1, 0, 1, 0, 0, 1, 1, 0, 2],
               [0, 1, 1, 1, 0, 1, 2, 0, 2],
               [0, 1, 2, 1, 1, 1, 1, 0, 0]]
    self.assertEqual(pond_sizes(terrain), {6, 3, 7})

if __name__ == "__main__":
  unittest.main()

