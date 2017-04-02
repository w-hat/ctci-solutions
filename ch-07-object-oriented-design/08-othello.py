# -*- coding: utf-8 -*-

# Design an Othello game.

import random

MOVE_DOTS = True
WHITE_SEARCH_DEPTH = 6     # None for human
BLACK_SEARCH_DEPTH = None  # None for human

DIRECTIONS = [(1, 0xFEFEFEFEFEFEFEFE), (-1, 0x7F7F7F7F7F7F7F7F),
              (8, 0xFFFFFFFFFFFFFFFF), (-8, 0xFFFFFFFFFFFFFFFF),
              (7, 0x7F7F7F7F7F7F7F7F), (-7, 0xFEFEFEFEFEFEFEFE),
              (9, 0xFEFEFEFEFEFEFEFE), (-9, 0x7F7F7F7F7F7F7F7F)]

EDGE   =  0x7E8181818181817E
CORNER =  0x8100000000000081
NOT_CN = -0x42c300000000c343
BLACK_START = (1<<27) | (1<<36)
WHITE_START = (1<<28) | (1<<35)

class Othello(object):
  def __init__(self, side=0, black=BLACK_START, white=WHITE_START):
    self.side = side
    self.bits = [black, white]
  
  def end_score(self):
    score = popcount(self.bits[self.side]) - popcount(self.bits[self.side^1])
    return score * 1024
  
  def evaluate(self):
    friendly, enemy = self.bits[self.side], self.bits[self.side^1]
    empty_n = neighbors(~(friendly | enemy))
    value = float(popcount(friendly & NOT_CN) - popcount(enemy & NOT_CN))
    value += 0.875 * float(count(friendly & EDGE) - count(enemy & EDGE))
    value += 8 * float(count(friendly & CORNER) - count(enemy & CORNER))
    value -= 1.5 * (popcount(friendly & empty_n) - popcount(enemy & empty_n))
    return value + random.random()
    
  def legal_moves(self):
    moves = []
    friendly, enemy = self.bits[self.side], self.bits[self.side^1]
    placement = self.bits[0] | self.bits[1]
    potential = neighbors(enemy) & ~placement
    while potential:
      move = potential & -potential
      potential ^= move
      for step, mask in DIRECTIONS:
        bit = shift(move, step) & mask & enemy
        if bit == 0:
          continue
        bit = shift(bit, step) & mask
        while bit & enemy:
          bit = shift(bit, step) & mask
        if bit & friendly:
          moves.append(move)
          break
    return moves
  
  def winner(self):
    if not len(self.legal_moves()):
      black_count = popcount(self.bits[0])
      white_count = popcount(self.bits[1])
      if black_count == white_count:
        return "Tie"
      elif black_count > white_count:
        return "Black"
      else:
        return "White"
    return None
  
  def make_move(self, row, col):
    if row < 0 or row > 7 or col < 0 or col > 7:
      raise Exception('Invalid location.')
    bit = 1 << (row * 8 + col)
    if not bit in self.legal_moves():
      raise Exception('Illegal move.')
    self.make_bit_move(bit)
  
  def make_bit_move(self, move):
    self.bits[self.side] |= move
    friendly, enemy = self.bits[self.side], self.bits[self.side^1]
    for step, mask in DIRECTIONS:
      bit = shift(move, step) & mask & enemy
      if bit == 0:
        continue
      bit = shift(bit, step) & mask
      while bit & enemy:
        bit = shift(bit, step) & mask
      if bit & friendly == 0:
        continue
      bit = shift(bit, -step)
      while bit & enemy:
        self.bits[0] ^= bit
        self.bits[1] ^= bit
        bit = shift(bit, -step)
    self.side ^= 1

  def negamax(self, depth):
    moves = self.legal_moves()
    if not depth:
      return moves[random.randint(0, len(moves) - 1)]
    best_move = moves[0]
    best_rating = float('-inf')
    solid_best_move = moves[0]
    solid_best_rating = float('-inf')
    for move in moves:
      rating = -self.ab_rate_move(move, depth, float('-inf'), -best_rating)
      if rating > best_rating:
        best_rating = rating
        best_move = move
    return best_move
  
  def ab_rate_move(self, move, depth, lower, upper):
    board = Othello(self.side, self.bits[0], self.bits[1])
    board.make_bit_move(move)
    if depth == 1:
      return board.evaluate()
    moves = board.legal_moves()
    if len(moves) == 0:
      return board.end_score()
    best_rating = float('-inf')
    new_lower = lower
    for m in moves:
      rating = -board.ab_rate_move(m, depth-1, -upper, -new_lower)
      if rating > best_rating:
        best_rating = rating
        if best_rating > new_lower:
          new_lower = best_rating
          if new_lower > upper:
            break
    return best_rating
    
  def __str__(self):
    moves = self.legal_moves()
    parts = ['\n  +-----------------+\n']
    for r in xrange(8):
      parts.append(' ' + str(8 - r) + '| ')
      for c in xrange(8):
        bit = 1 << (r * 8 + c)
        if bit & self.bits[0]:             parts.append('○ ')
        elif bit & self.bits[1]:           parts.append('● ')
        elif MOVE_DOTS and (bit in moves): parts.append('. ')
        else:                              parts.append('  ')
      parts.append('|\n')
    parts.append('  +-----------------+\n')
    parts.append('    a b c d e f g h\n\n')
    return "".join(parts)

def popcount(bits):
  counts = (bits   & 0x5555555555555555) + ((bits   & 0xAAAAAAAAAAAAAAAA) >> 1)
  counts = (counts & 0x3333333333333333) + ((counts & 0xCCCCCCCCCCCCCCCC) >> 2)
  counts = (counts & 0x0F0F0F0F0F0F0F0F) + ((counts & 0xF0F0F0F0F0F0F0F0) >> 4)
  counts = (counts & 0x00FF00FF00FF00FF) + ((counts & 0xFF00FF00FF00FF00) >> 8)
  counts = (counts & 0x0000FFFF0000FFFF) + ((counts & 0xFFFF0000FFFF0000) >> 16)
  counts = (counts & 0x00000000FFFFFFFF) + (counts >> 32)
  return counts

def count(bits):
  count = 0
  while bits:
    bits &= bits - 1
    count += 1
  return count

def neighbors(bits):
  nbits  = (bits << 1) & 0xFEFEFEFEFEFEFEFE
  nbits |= (bits >> 1) & 0x7F7F7F7F7F7F7F7F
  nbits |= (bits << 9) & 0xFEFEFEFEFEFEFEFE
  nbits |= (bits << 7) & 0x7F7F7F7F7F7F7F7F
  nbits |= (bits >> 7) & 0xFEFEFEFEFEFEFEFE
  nbits |= (bits >> 9) & 0x7F7F7F7F7F7F7F7F
  nbits |= (bits << 8) & 0xFFFFFFFFFFFFFFFF
  return nbits | (bits >> 8)

def shift(bits, step):
  if step > 0:
    return bits << step
  return bits >> -step

def play_game():
  board = Othello()
  while len(board.legal_moves()):
    if board.side:
      if not WHITE_SEARCH_DEPTH is None:
        print(str(board) + 'The computer is making a move for ●.')
        board.make_bit_move(board.negamax(WHITE_SEARCH_DEPTH))
        continue
    elif not BLACK_SEARCH_DEPTH is None:
      print(str(board) + 'The computer is making a move for ○.')
      board.make_bit_move(board.negamax(BLACK_SEARCH_DEPTH))
      continue
    if board.side:
      prompt = 'Choose where to place a ●. (ie "d3")\n> '
    else:
      prompt = 'Choose where to place a ○. (ie "d3")\n> '
    line = raw_input(str(board) + prompt)
    try:
      row = 8 - int(line[1])
      col = ord(line[0]) - 97
      board.make_move(row, col)
    except Exception as e:
      print(e)
  print(str(board))
  winner = board.winner()
  if winner == "Tie":
    print("The game is a tie!")
  elif winner == "Black":
    print("○ wins!")
  else:
    print("● wins!")
  return winner

if __name__ == "__main__":
  import sys
  if sys.argv[-1] == 'play':
    play_game()
  else:
    import unittest
    class Test(unittest.TestCase):
      def test_othello(self):
        board = Othello()
        self.assertEqual(board.side, 0)
        self.assertEqual(board.end_score(), 0)
        self.assertEqual(len(board.legal_moves()), 4)
        board.make_bit_move(board.legal_moves()[0])
        self.assertEqual(board.side, 1)
        self.assertEqual(len(board.legal_moves()), 3)
        board = Othello(1, 0x2040c08000000, 0x181010000000)
        self.assertEqual(board.negamax(1), (1 << 56))
        self.assertEqual(board.negamax(2), (1 << 56))
        self.assertEqual(board.negamax(3), (1 << 56))
    unittest.main()

