# Determine if a game of tic-tac-toe is over.

def tic_tac_win(board):
  n = len(board)
  if n == 0:
    return 0
  row_results  = [0] * n
  col_results  = [0] * n
  diag_results = [0] * 2
  for r in xrange(n):
    for c in xrange(n):
      if board[r][c] == "o":
        bit_mask = 0b10
      elif board[r][c] == "x":
        bit_mask = 0b01
      else:
        bit_mask = 0b11
      row_results[r] |= bit_mask
      col_results[c] |= bit_mask
      if r == c:
        diag_results[0] |= bit_mask
      if r == n - c:
        diag_results[1] |= bit_mask
    if row_results[r] != 0b11:
      return row_results[r]
  for c in xrange(n):
    if col_results[c] != 0b11:
      return col_results[c]
  for d in xrange(2):
    if diag_results[d] != 0b11:
      return diag_results[d]
  return 0

import unittest

class Test(unittest.TestCase):
  def test_tic_tac_win(self):
    board = [["o", "o", "o"],
             ["x", "x", " "],
             [" ", "x", "x"]]
    self.assertEqual(tic_tac_win(board), 0b10)
    board[0][0] = "x"
    self.assertEqual(tic_tac_win(board), 0b01)
    board[1][1] = "o"
    self.assertEqual(tic_tac_win(board), 0b00)
    board = [["o", "o", "o", "x"],
             ["x", "x", "o", "o"],
             ["x", " ", "x", "x"],
             ["o", "x", "o", "x"]]
    self.assertEqual(tic_tac_win(board), 0b00)
    board[0][3] = "o"
    self.assertEqual(tic_tac_win(board), 0b10)
    board[0][0] = "x"
    self.assertEqual(tic_tac_win(board), 0b01)
    board[2][2] = "o"
    self.assertEqual(tic_tac_win(board), 0b10)

if __name__ == "__main__":
  unittest.main()

