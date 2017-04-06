# Implement a simple calculator.

def calculate(string):
  #return eval(string)
  tokens = tokenize(string)
  if len(tokens) == 0:
    return None
  products = []
  i = 0
  while i < len(tokens):
    if tokens[i] == "*":
      products[-1] *= tokens[i+1]
      i += 2
    elif tokens[i] == "/":
      products[-1] /= tokens[i+1]
      i += 2
    else:
      products.append(tokens[i])
      i += 1
  result = products[0]
  for i in xrange(1, len(products) - 1, 2):
    if products[i] == "+":
      result += products[i+1]
    elif products[i] == "-":
      result -= products[i+1]
    else:
      raise Exception("Unknown operation.")
  return result

def tokenize(string):
  number_start = 0
  tokens = []
  for i, char in enumerate(string):
    if char in "+-*/":
      if number_start == i:
        raise Exception("Missing number between operators")
      tokens.append(int(string[number_start:i]))
      tokens.append(char)
      number_start = i+1
    elif not char in "0123456789":
      raise Exception("Unknown character")
  tokens.append(int(string[number_start:]))
  return tokens

import unittest

class Test(unittest.TestCase):
  def test_calculate(self):
    self.assertEqual(calculate("1+1"), 2)
    self.assertEqual(calculate("0+4"), 4)
    self.assertEqual(calculate("0*7"), 0)
    self.assertEqual(calculate("9*0+1"), 1)
    self.assertEqual(calculate("1+1+1"), 3)
    self.assertEqual(calculate("1+6/5"), 2)
    self.assertEqual(calculate("3+7/8*7"), 3)
    self.assertEqual(calculate("1+11"), 12)
    self.assertEqual(calculate("200+423"), 623)

if __name__ == "__main__":
  unittest.main()

