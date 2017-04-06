# Implement operations with only addition (and negation).

def multiply(a, b):
  if abs(a) < abs(b):
    s, l = a, b
  else:
    s, l = b, a
  product = 0
  for _ in xrange(abs(s)):
    product += l
  if s < 0:
    return -product
  return product

def divide(a, b):
  if b == 0:
    return None
  product = 0
  quotient = 0
  while product + abs(b) < abs(a) + 1:
    product += abs(b)
    quotient += 1
  if int(a < 0) + int(b < 0) == 1:
    return -quotient
  return quotient

def subtract(a, b):
  return a + (-b)

import unittest

class Test(unittest.TestCase):
  def test_multiply(self):
    self.assertEqual(multiply(3, 6), 18)
    self.assertEqual(multiply(7, 11), 77)
    self.assertEqual(multiply(-8, 10), -80)
  
  def test_divide(self):
    self.assertEqual(divide(3, 6), 0)
    self.assertEqual(divide(30, 6), 5)
    self.assertEqual(divide(34, -6), -5)
    self.assertEqual(divide(120, 10), 12)
  
  def test_subtract(self):
    self.assertEqual(subtract(34, 6), 28)
    self.assertEqual(subtract(31, -6), 37)

if __name__ == "__main__":
  unittest.main()

