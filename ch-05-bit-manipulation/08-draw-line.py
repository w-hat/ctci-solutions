# Draw a horizontal line from (x_1, y) to (x_2, y).

def draw_line(screen, width, x1, x2, y):
  byte_width = width / 8
  height = len(screen) / byte_width
  if x1 < x2:
    x_start, x_end = x1, x2
  else:
    x_start, x_end = x2, x1
  if x_start < 0 or x_end > width or y > height:
    return None
  byte = y * byte_width + x_start / 8
  byte_end = y * byte_width + x_end / 8
  screen[byte] = (1 << (x_start % 8)) - 1
  byte += 1
  while byte < byte_end:
    screen[byte] = 255
    byte += 1
  screen[byte] = 255 ^ ((1 << (x_end % 8)) - 1)

import unittest

class Test(unittest.TestCase):
  def test_draw_line(self):
    screen = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0]
    draw_line(screen, 64, 20, 42, 1)
    self.assertEqual(screen, [0]*8 + [0, 0, 15, 255, 255, 252, 0, 0] + [0]*8)

if __name__ == "__main__":
  unittest.main()

