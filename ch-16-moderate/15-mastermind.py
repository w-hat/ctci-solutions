# Determine the number of hits and pseudohits for a guess in Mastermind.

COLOR_IX = {'B': 0, 'Y': 1, 'G': 2, 'R': 3}

def mastermind_hits(code, guess):
  hit_count, pseudohit_count = 0, 0
  colors_included = [0] * 4
  colors_hit  = [0] * 4
  colors_guessed = [0] * 4
  for i in xrange(4):
    code_color = COLOR_IX[code[i]]
    guess_color = COLOR_IX[guess[i]]
    if code[i] == guess[i]:
      hit_count += 1
      colors_hit[code_color] = 1
    colors_included[code_color] = 1
    colors_guessed[guess_color] = 1
  for i in xrange(4):
    pseudohit_count += colors_guessed[i] & colors_included[i] & ~colors_hit[i]
  return (hit_count, pseudohit_count)

import unittest

class Test(unittest.TestCase):
  def test_mastermind_hits(self):
    self.assertEqual(mastermind_hits("YYBB", "BBYY"), (0, 2))
    self.assertEqual(mastermind_hits("BYBB", "BBYY"), (1, 1))
    self.assertEqual(mastermind_hits("RGBY", "RGBY"), (4, 0))
    self.assertEqual(mastermind_hits("RGBY", "RBGY"), (2, 2))
    self.assertEqual(mastermind_hits("RGBY", "RRRR"), (1, 0))
    self.assertEqual(mastermind_hits("RRRR", "RBGY"), (1, 0))
    self.assertEqual(mastermind_hits("RRYY", "RYGY"), (2, 0))

if __name__ == "__main__":
  unittest.main()

