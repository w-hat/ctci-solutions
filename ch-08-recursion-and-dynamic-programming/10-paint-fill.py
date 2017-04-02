# Fill in the region containing the point with the given color.

def paint_fill(image, x, y, color):
  if x < 0 or y < 0 or len(image) <= y or len(image[y]) <= x:
    return
  old_color = image[y][x]
  if old_color == color:
    return
  paint_fill_color(image, x, y, color, old_color)

def paint_fill_color(image, x, y, new_color, old_color):
  if image[y][x] != old_color:
    return
  image[y][x] = new_color
  if y > 0:
    paint_fill_color(image, x, y - 1, new_color, old_color)
  if y < len(image) - 1:
    paint_fill_color(image, x, y + 1, new_color, old_color)
  if x > 0:
    paint_fill_color(image, x - 1, y, new_color, old_color)
  if x < len(image[y]) - 1:
    paint_fill_color(image, x + 1, y, new_color, old_color)

import unittest

class Test(unittest.TestCase):
  def test_paint_fill(self):
    image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
              [30, 20, 20, 10, 10, 40, 40, 40],
              [10, 10, 20, 20, 10, 10, 10, 10],
              [10, 10, 30, 20, 20, 20, 20, 10],
              [40, 40, 10, 10, 10, 10, 10, 10]]
    image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [10, 10, 20, 20, 30, 30, 30, 30],
              [10, 10, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
              [30, 20, 20, 30, 30, 40, 40, 40],
              [30, 30, 20, 20, 30, 30, 30, 30],
              [30, 30, 30, 20, 20, 20, 20, 30],
              [40, 40, 30, 30, 30, 30, 30, 30]]
    paint_fill(image1, 3, 1, 30)
    self.assertEqual(image1, image2)
    paint_fill(image1, 3, 1, 10)
    paint_fill(image1, 3, 1, 30)
    self.assertEqual(image1, image3)

if __name__ == "__main__":
  unittest.main()

