# Design Minesweeper.

class Minesweeper(object):
  def __init__(self, rows, cols, bombs_count=None):
    self.rows, self.cols = rows, cols
    self.game_over = False
    self.game_won = False
    self.bombs_found = 0
    self.bombs_count = bombs_count
    if not self.bombs_count:
      self.bombs_count = (rows * cols + 10) / 10
    self.bombs    = [[0 for r in xrange(rows+2)] for c in xrange(cols+2)]
    self.counts   = [[0 for r in xrange(rows+2)] for c in xrange(cols+2)]
    self.revealed = [[0 for r in xrange(rows+2)] for c in xrange(cols+2)]
    for i in xrange(self.bombs_count):
      bomb_row = random.randint(1, rows)
      bomb_col = random.randint(1, cols)
      if not self.bombs[bomb_row][bomb_col]:
        self.bombs[bomb_row][bomb_col] = 1
        for row in [bomb_row-1, bomb_row, bomb_row+1]:
          for col in [bomb_col-1, bomb_col, bomb_col+1]:
            self.counts[row][col] += 1
  
  def __str__(self):
    line1, line2, line3 = "    ", "    ", "    "
    for c in xrange(1, self.cols+1):
      label = str(c)
      while len(label) < 3:
        label = " " + label
      line1 += " " + label[0]
      line2 += " " + label[1]
      line3 += " " + label[2]
    parts = [line1, '\n', line2, '\n', line3, '\n']
    parts.append(('   +' + '-' * (2*self.cols+1)) + '+\n')
    for r in xrange(1, self.rows+1):
      label = str(r)
      while len(label) < 3:
        label = " " + label
      parts += label + '| '
      for c in xrange(1, self.cols+1):
        if self.revealed[r][c]:
          if self.bombs[r][c]:
            parts.append("B ")
          elif self.counts[r][c]:
            parts.append(str(self.counts[r][c]) + " ")
          else:
            parts.append("  ")
        else:
          parts.append(". ")
      parts += '|\n'
    parts += ['   +' + ('-' * (2*self.cols+1)) + '+\n']
    return "".join(parts)
  
  def mark_clear(self, row, col):
    if row < 1 or row > self.rows or col < 1 or col > self.cols:
      return
    if self.revealed[row][col]:
      return
    self.revealed[row][col] = True
    if self.bombs[row][col]:
      self.game_over = True
    elif self.counts[row][col] == 0:
      for r in xrange(row - 1, row + 2):
        for c in xrange(col - 1, col + 2):
          self.mark_clear(r, c)
      
  
  def mark_bomb(self, row, col):
    self.revealed[row][col] = True
    if not self.bombs[row][col]:
      self.game_over = True
    else:
      self.bombs_found += 1
      if self.bombs_found == self.bombs_count:
        self.game_won = True
        self.game_over = True
  
prompt = "Enter row,col to clear and bomb,row,col to label a bomb.\n> "

def play_game():
  rows = int(sys.argv[-2])
  cols = int(sys.argv[-1])
  minesweeper = Minesweeper(rows, cols)
  while not minesweeper.game_over:
    line = raw_input(str(minesweeper) + prompt)
    try:
      coords = line.split(",")
      if coords[0].strip().lower() == "bomb":
        row, col = int(coords[1]), int(coords[2])
        minesweeper.mark_bomb(row, col)
      else:
        row, col = int(coords[0]), int(coords[1])
        minesweeper.mark_clear(row, col)
    except Exception as e:
      print(e)
  print(str(minesweeper))
  if minesweeper.game_won:
    print("You win!")
  else:
    print("You lose.")


class MockRandom(object):
  def __init__(self):
    self.values = [1, 3, 1, 1]
    
  def randint(self, lower, upper):
    return self.values.pop(0)

if __name__ == "__main__":
  import sys
  if len(sys.argv) > 2 and sys.argv[-3] == "play":
    import random
    play_game()
  else:
    import unittest
    print("Use the option --play {rows} {cols} to play Minesweeper.")
    global random
    random = MockRandom()
    
    class Test(unittest.TestCase):
      def test_minesweeper(self):
        m = Minesweeper(4, 4)
        self.assertEqual(m.bombs, [[0, 0, 0, 0, 0, 0],
                                   [0, 1, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0]])
    unittest.main()

