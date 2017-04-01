# Test chess movement.

CARDINAL = [
  lambda b: (b << 1) & 0xFEFEFEFEFEFEFEFE,
  lambda b: (b >> 1) & 0x7F7F7F7F7F7F7F7F,
  lambda b: (b << 8) & 0xFFFFFFFFFFFFFFFF,
  lambda b: (b >> 8)]
DIAGONAL = [
  lambda b: (b << 7) & 0x7F7F7F7F7F7F7F7F,
  lambda b: (b >> 7) & 0xFEFEFEFEFEFEFEFE,
  lambda b: (b << 9) & 0xFEFEFEFEFEFEFEFE,
  lambda b: (b >> 9) & 0x7F7F7F7F7F7F7F7F]
KNIGHTAL = [
  lambda b: (b << 10) & 0xFCFCFCFCFCFCFC00,
  lambda b: (b >> 10) & 0x3F3F3F3F3F3F3F,
  lambda b: (b << 15) & 0x7F7F7F7F7F7F0000,
  lambda b: (b >> 15) & 0xFEFEFEFEFEFE,
  lambda b: (b << 17) & 0xFEFEFEFEFEFE0000,
  lambda b: (b >> 17) & 0x7F7F7F7F7F7F,
  lambda b: (b << 6)  & 0x3F3F3F3F3F3F3F00,
  lambda b: (b >> 6)  & 0xFCFCFCFCFCFCFC]

EMPTY    = 0
W_PAWN   = 1
W_KNIGHT = 2
W_BISHOP = 3
W_ROOK   = 4
W_QUEEN  = 5
W_KING   = 6
B_PAWN   = 7
B_KNIGHT = 8
B_BISHOP = 9
B_ROOK   = 10
B_QUEEN  = 11
B_KING   = 12

PIECE_CHARS = " pnbrqkPNBRQK"

def neighbors(bit):
  neighbors = 0
  for step in CARDINAL:
    neighbors |= step(bit)
  for step in DIAGONAL:
    neighbors |= step(bit)
  return neighbors

class ChessBoard(object):
  def __init__(self, string=None, side=0, bits=None):
    if string is None:
      self.side = side
      if bits is None:
        self.bits = [0xFFFFFFFF0000,
                     0xFF000000000000,   0x4200000000000000, 0x2400000000000000,
                     0x8100000000000000, 0x800000000000000,  0x1000000000000000,
                     0xFF00, 0x42, 0x24, 0x81, 0x8, 0x10]
      else:
        self.bits = bits
    else:
      string = string.strip()
      self.side = int(string[0] == 'B')
      self.bits = [0xFFFFFFFFFFFFFFFF, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      lines = string.split("\n")
      for row, line in enumerate(lines[2:10]):
        line = line.strip()
        for col in xrange(0, 8):
          bit = 1 << (row * 8 + col)
          piece_char = line[3 + col * 2]
          piece = PIECE_CHARS.index(piece_char)
          if piece == -1:
            raise Exception("Bad piece character {}.".format(piece_char))
          self.bits[EMPTY] ^= bit
          self.bits[piece] ^= bit
  
  def legal_moves(self):
    moves = []
    offset = self.side * 6
    # Pawns
    friendly_pawn = W_PAWN + offset
    pawns = self.bits[friendly_pawn]
    if self.side:
      pawn_step = CARDINAL[2]
      pawn_start_row = 0xFF00
    else:
      pawn_step = CARDINAL[3]
      pawn_start_row = 0xFF000000000000
    # TODO En passant.
    while pawns:
      pawn = pawns & -pawns
      pawns ^= pawn
      front = pawn_step(pawn)
      if front & self.bits[EMPTY]:
        self.try_move(moves, friendly_pawn, pawn, front)
        if pawn & pawn_start_row:
          double = pawn_step(front)
          if double & self.bits[EMPTY]:
            self.try_move(moves, friendly_pawn, pawn, double)
      right = CARDINAL[0](front)
      if right & ~self.bits[EMPTY]:
        self.try_move(moves, friendly_pawn, pawn, right)
      left = CARDINAL[1](front)
      if left & ~self.bits[EMPTY]:
        self.try_move(moves, friendly_pawn, pawn, left)
    # Knights
    friendly_knight = W_KNIGHT + offset
    knights = self.bits[friendly_knight]
    while knights:
      knight = knights & -knights
      knights ^= knight
      for knight_move in KNIGHTAL:
        self.try_move(moves, friendly_knight, knight, knight_move(knight))
    # Bishops
    friendly_bishop = W_BISHOP + offset
    bishops = self.bits[friendly_bishop]
    while bishops:
      bishop = bishops & -bishops
      bishops ^= bishop
      for diagonal_step in DIAGONAL:
        move = diagonal_step(bishop)
        while move & self.bits[EMPTY]:
          self.try_move(moves, friendly_bishop, bishop, move)
          move = diagonal_step(move)
        self.try_move(moves, friendly_bishop, bishop, move)
    # Rooks
    friendly_rook = W_ROOK + offset
    rooks = self.bits[friendly_rook]
    while rooks:
      rook = rooks & -rooks
      rooks ^= rook
      for cardinal_step in CARDINAL:
        move = cardinal_step(rook)
        while move & self.bits[EMPTY]:
          self.try_move(moves, friendly_rook, rook, move)
          move = cardinal_step(move)
        self.try_move(moves, friendly_rook, rook, move)
    # Queens
    friendly_queen = W_QUEEN + offset
    queens = self.bits[friendly_queen]
    while queens:
      queen = queens & -queens
      queens ^= queen
      for diagonal_step in DIAGONAL:
        move = diagonal_step(queen)
        while move & self.bits[EMPTY]:
          self.try_move(moves, friendly_queen, queen, move)
          move = diagonal_step(move)
        self.try_move(moves, friendly_queen, queen, move)
      for cardinal_step in CARDINAL:
        move = cardinal_step(queen)
        while move & self.bits[EMPTY]:
          self.try_move(moves, friendly_queen, queen, move)
          move = cardinal_step(move)
        self.try_move(moves, friendly_queen, queen, move)
    # King
    friendly_king = W_KING + offset
    king = self.bits[friendly_king]
    # TODO Castling
    for diagonal_step in DIAGONAL:
      self.try_move(moves, friendly_king, king, diagonal_step(king))
    for cardinal_step in CARDINAL:
      self.try_move(moves, friendly_king, king, cardinal_step(king))
    return moves
  
  def try_move(self, moves, piece, from_bit, to_bit):
    # Make sure that a friendly piece is not being stepped on.
    to_bit_piece = EMPTY
    enemy = (self.side ^ 1) * 6
    if not (to_bit & self.bits[EMPTY]):
      friendly_pawn = W_PAWN + self.side * 6
      if to_bit & self.bits[friendly_pawn]:
        return
      enemy_pawn = W_PAWN + enemy
      for enemy_piece in xrange(enemy_pawn, enemy_pawn + 5):
        if to_bit & self.bits[enemy_piece]:
          to_bit_piece = enemy_piece
          break
      if to_bit_piece == EMPTY:
        return
    # Try making the move.
    # TODO Handle promotions.
    self.bits[piece] ^= from_bit | to_bit
    self.bits[EMPTY] ^= from_bit
    self.bits[to_bit_piece] ^= to_bit
    # Check for check.
    legal = not self.in_check()
    # Undo the move.
    self.bits[piece] ^= from_bit | to_bit
    self.bits[EMPTY] ^= from_bit
    self.bits[to_bit_piece] ^= to_bit
    if legal:
      moves.append((piece, from_bit, to_bit, to_bit_piece))
  
  def in_check(self):
    enemy = (self.side ^ 1) * 6
    king = self.bits[W_KING + self.side * 6]
    for diagonal_step in DIAGONAL:
      move = diagonal_step(king)
      while move & self.bits[EMPTY]:
        move = diagonal_step(move)
      if move and move & (self.bits[W_BISHOP+enemy] | self.bits[W_QUEEN+enemy]):
        return True
    for cardinal_step in CARDINAL:
      move = cardinal_step(king)
      while move & self.bits[EMPTY]:
        move = cardinal_step(move)
      if move and move & (self.bits[W_ROOK+enemy] | self.bits[W_QUEEN+enemy]):
        return True
    for knight_move in KNIGHTAL:
      if knight_move(king) & self.bits[W_KNIGHT+enemy]:
        return True
    if self.side:
      if (DIAGONAL[0](king) | DIAGONAL[2](king)) & self.bits[W_PAWN+enemy]:
        return True
    else:
      if (DIAGONAL[1](king) | DIAGONAL[3](king)) & self.bits[W_PAWN+enemy]:
        return True
    return bool(neighbors(king) & self.bits[W_KING+enemy])
  
  def make_move(self, from_row, from_col, to_row, to_col):
    from_bit = 1 << (from_row * 8 + from_col)
    to_bit = 1 << (to_row * 8 + to_col)
    friendly = self.side * 6
    piece = EMPTY
    if from_bit & self.bits[EMPTY]:
      raise Exception("Cannot move from an empty square.")
    for p in xrange(W_PAWN + friendly, W_KING + friendly + 1):
      if from_bit & self.bits[p]:
        piece = p
        break
    if piece == EMPTY:
      raise Exception("Must move a friendly piece.")
    to_bit_piece = EMPTY
    if not (to_bit & self.bits[EMPTY]):
      enemy = (self.side ^ 1) * 6
      for p in xrange(W_PAWN + enemy, W_KING + enemy):
        if to_bit & self.bits[p]:
          to_bit_piece = p
          break
    move = (piece, from_bit, to_bit, to_bit_piece)
    if not move in self.legal_moves():
      raise Exception("Illegal move.")
    self.make_bit_move(piece, from_bit, to_bit, to_bit_piece)
  
  def make_bit_move(self, piece, from_bit, to_bit, to_bit_piece):
    self.bits[piece] ^= from_bit | to_bit
    self.bits[EMPTY] ^= from_bit
    self.bits[to_bit_piece] ^= to_bit
    self.side ^= 1
    # TODO Castling and en passant and promotion repetition.
  
  def __eq__(self, other):
    return self.side == other.side and self.bits == other.bits
    # TODO Add additional castling and en passant data.
  
  def __str__(self):
    parts = []
    if self.side:
      parts.append("\nB\n")
    else:
      parts.append("\nw\n")
    parts.append('  +-----------------+\n')
    for r in xrange(8):
      parts.append(' ' + str(8 - r) + '| ')
      for c in xrange(8):
        bit = 1 << (r * 8 + c)
        if   bit & self.bits[0]:  parts.append('  ')
        elif bit & self.bits[1]:  parts.append('p ')
        elif bit & self.bits[2]:  parts.append('n ')
        elif bit & self.bits[3]:  parts.append('b ')
        elif bit & self.bits[4]:  parts.append('r ')
        elif bit & self.bits[5]:  parts.append('q ')
        elif bit & self.bits[6]:  parts.append('k ')
        elif bit & self.bits[7]:  parts.append('P ')
        elif bit & self.bits[8]:  parts.append('N ')
        elif bit & self.bits[9]:  parts.append('B ')
        elif bit & self.bits[10]: parts.append('R ')
        elif bit & self.bits[11]: parts.append('Q ')
        elif bit & self.bits[12]: parts.append('K ')
        else:                     parts.append('? ')
      parts.append('|\n')
    parts.append('  +-----------------+\n')
    parts.append('    a b c d e f g h\n\n')
    return "".join(parts)

def play():
  board = ChessBoard()
  legal_moves = board.legal_moves()
  while len(legal_moves):
    prompt = 'Enter a move. (ie "c2c4")\n> '
    line = raw_input(str(board) + prompt)
    try:
      from_row = 8 - int(line[1])
      from_col = ord(line[0]) - 97
      to_row = 8 - int(line[3])
      to_col = ord(line[2]) - 97
      board.make_move(from_row, from_col, to_row, to_col)
    except Exception as e:
      print(e)
    legal_moves = board.legal_moves()

if __name__ == "__main__":
  import sys
  if sys.argv[-1] == "play":
    play()
  else:
    import unittest
    class Test(unittest.TestCase):
      def test_chess_board_init(self):
        board = ChessBoard()
        self.assertEqual(board, ChessBoard(side=board.side, bits=board.bits[:]))
        self.assertEqual(board, ChessBoard(string=str(board)))
      
      def test_chess_board_initial_moves(self):
        board = ChessBoard()
        self.assertEqual(len(board.legal_moves()), 20)
        
      def test_chess_board_knight_moves(self):
        board = ChessBoard("""w
         +-----------------+
        8|         K       |
        7|               P |
        6|               p |
        5|             k   |
        4|       n         |
        3|                 |
        2|                 |
        1|                 |
         +-----------------+
           a b c d e f g h""")
        moves = board.legal_moves()
        self.assertEqual(len(moves), 14)
        knight_moves = 0
        for move in moves:
          if move[0] == W_KNIGHT:
            knight_moves |= move[2]
        self.assertEqual(knight_moves, 0x14220022140000)
      
      def test_chess_board_queen_moves(self):
        board = ChessBoard("""w
         +-----------------+
        8|         K       |
        7|             k P |
        6|               p |
        5|                 |
        4|       q         |
        3|                 |
        2|                 |
        1|                 |
         +-----------------+
           a b c d e f g h""")
        moves = board.legal_moves()
        self.assertEqual(len(moves), 29)
        queen_moves = 0
        for move in moves:
          if move[0] == W_QUEEN:
            queen_moves |= move[2]
        self.assertEqual(queen_moves, 0x492a1cf71c2a0908)
      
      def test_chess_board_in_check_moves(self):
        board = ChessBoard("""w
         +-----------------+
        8|       n K     Q |
        7|               P |
        6|   R           k |
        5| b               |
        4|       r   r     |
        3|         B       |
        2|                 |
        1|                 |
         +-----------------+
           a b c d e f g h""")
        moves = board.legal_moves()
        self.assertEqual(len(moves), 6)
      
      def test_chess_board_legal_moves(self):
        board = ChessBoard("""w
         +-----------------+
        8| R N B   K B   R |
        7| P P   P Q P P P |
        6|     P           |
        5|       N     n   |
        4| q   p p P       |
        3|           p     |
        2| p p     p   p p |
        1| r n b   k b   r |
         +-----------------+
           a b c d e f g h""")
        self.assertEqual(len(board.legal_moves()), 37)
        board.side = 1
        self.assertEqual(len(board.legal_moves()), 32)
    unittest.main()

