# Stack boxes as high as possible.

def stack_boxes(boxes):
  sorted_boxes = sorted(boxes, lambda a, b: a.height > b.height)
  return stack_more_boxes(sorted_boxes, None, 0)

def stack_more_boxes(boxes, base, index):
  if index >= len(boxes):
    return 0
  without_box_height = stack_more_boxes(boxes, base, index + 1)
  box = boxes[index]
  if (not base) or box.fits_on(base):
    with_box_height = box.height + stack_more_boxes(boxes, box, index + 1)
    if with_box_height > without_box_height:
      return with_box_height
  return without_box_height

class Box(object):
  def __init__(self, height, width, depth):
    self.height, self.width, self.depth = height, width, depth
  
  def fits_on(self, base):
    return base.height > self.height and \
           base.width  > self.width  and \
           base.depth  > self.depth

import unittest

class Test(unittest.TestCase):
  def test_stack_boxes(self):
    boxes = [Box(100, 100, 100)]
    self.assertEqual(stack_boxes(boxes), 100)
    boxes.append(Box(25, 25, 25))
    self.assertEqual(stack_boxes(boxes), 125)
    boxes.append(Box(20, 5, 30))
    boxes.append(Box(17, 4, 28))
    self.assertEqual(stack_boxes(boxes), 137)

if __name__ == "__main__":
  unittest.main()

