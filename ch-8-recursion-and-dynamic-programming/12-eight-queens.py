# Find all arrangements of eight queens on a chess board that cannot attack
# each other.

STEPS = [
  lambda b: (b << 1) & 0xFEFEFEFEFEFEFEFE,
  lambda b: (b << 7) & 0x7F7F7F7F7F7F7F7F,
  lambda b: (b << 9) & 0xFEFEFEFEFEFEFEFE,
  lambda b: (b << 8) & 0xFFFFFFFFFFFFFFFF,
  lambda b: (b >> 1) & 0x7F7F7F7F7F7F7F7F,
  lambda b: (b >> 7) & 0xFEFEFEFEFEFEFEFE,
  lambda b: (b >> 9) & 0x7F7F7F7F7F7F7F7F,
  lambda b: (b >> 8)]

def eight_queens():
  return eight_queens_partial(0, -1, 0xFF00000000000000)

def eight_queens_partial(queens, available, row):
  if row == 0:
    return [queens]
  placements = []
  possibility = available & row
  next_row = row >> 8
  while possibility:
    queen = possibility & -possibility
    possibility ^= queen
    next_queens = queens | queen
    next_available = available & ~queen_reach(queen)
    placements += eight_queens_partial(next_queens, next_available, next_row)
  return placements

def queen_reach(bit):
  reach = bit
  for step in STEPS:
    move = bit
    while move:
      reach |= move
      move = step(move)
  return reach

def show(placement):
  parts = ["\n+-----------------+\n"]
  for row in xrange(8):
    parts.append('| ')
    for col in xrange(8):
      bit = 1 << (row * 8 + col)
      if bit & placement:
        parts.append('Q ')
      else:
        parts.append('  ')
    parts.append('|\n')
  parts.append("+-----------------+\n")
  return "".join(parts)

import unittest

class Test(unittest.TestCase):
  def test_eight_queens(self):
    placements = eight_queens()
    self.assertEqual(len(placements), 92)
    self.assertEqual(show(placements[0]), """
+-----------------+
|       Q         |
|   Q             |
|             Q   |
|     Q           |
|           Q     |
|               Q |
|         Q       |
| Q               |
+-----------------+
""")

if __name__ == "__main__":
  unittest.main()

