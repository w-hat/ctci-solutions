# Design a jigsaw puzzle.

import random

class Puzzle(object):
  def __init__(self, n):
    pieces = [[Piece() for r in xrange(n)] for c in xrange(n)]
    for r in xrange(n):
      for c in xrange(n):
        if r:
          pieces[r][c].fit_with(pieces[r-1][c])
        if c:
          pieces[r][c].fit_with(pieces[r][c-1])
    self.pieces = sum(pieces, [])
    for i, _ in enumerate(self.pieces):
      j = random.randint(0, len(pieces)-1)
      self.pieces[i], self.pieces[j] = self.pieces[j], self.pieces[i]
  
  def is_solved(self):
    for piece in self.pieces:
      if piece.connected != piece.fits:
        return False
    return True

def solve(puzzle):
  for piece in puzzle.pieces:
    for other in puzzle.pieces:
      if other in piece.fits:
        piece.connect(other)

class Piece(object):
  def __init__(self):
    self.fits = set()
    self.connected = set()
  
  def fit_with(self, other):
    self.fits.add(other)
    other.fits.add(self)
  
  def connect(self, other):
    self.connected.add(other)
    other.connected.add(self)

import unittest

class Test(unittest.TestCase):
  def test_puzzle(self):
    puzzle = Puzzle(20)
    self.assertEqual(puzzle.is_solved(), False)
    solve(puzzle)
    self.assertEqual(puzzle.is_solved(), True)

if __name__ == "__main__":
  unittest.main()

