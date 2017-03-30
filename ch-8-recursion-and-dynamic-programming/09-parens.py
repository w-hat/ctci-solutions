# List all valid strings containing n opening and n closing parenthesis.

# Note that parens1 happens to be faster and more space efficient than parens2,
# which is faster than parens3.  The slowest is parens4 only because it is not
# memoized.

def parens1(n):
  parens_of_length = [[""]]
  if n == 0:
    return parens_of_length[0]
  for length in xrange(1, n + 1):
    parens_of_length.append([])
    for i in xrange(length):
      for inside in parens_of_length[i]:
        for outside in parens_of_length[length - i - 1]:
          parens_of_length[length].append("(" + inside + ")" + outside)
  return parens_of_length[n]

def parens2(n, open_count=0, close_count=0, memo=None):
  if open_count + close_count == 2 * n:
    return [""]
  key = (n - open_count - close_count, open_count)
  if memo is None:
    memo = {}
  elif key in memo:
    return memo[key]
  parens = []
  if open_count < n:
    parens += ["(" + end for end in parens2(n, open_count+1, close_count, memo)]
  if close_count < open_count:
    parens += [")" + end for end in parens2(n, open_count, close_count+1, memo)]
  memo[key] = parens
  return parens

def parens3(n):
  return parens_memo3(n, 0, 0, {})

def parens_memo3(n, open_count, close_count, memo):
  if open_count + close_count == 2 * n:
    return [""]
  key = (n - open_count - close_count, open_count)
  if key in memo:
    return memo[key]
  parens = []
  if open_count < n:
    for end in parens_memo3(n, open_count + 1, close_count, memo):
      parens.append("(" + end)
  if close_count < open_count:
    for end in parens_memo3(n, open_count, close_count + 1, memo):
      parens.append(")" + end)
  memo[key] = parens
  return parens

def parens4(n, partial="", open_count=0, close_count=0):
  if open_count + close_count == 2 * n:
    return [partial]
  parens = []
  if open_count < n:
    parens += parens4(n, partial + "(", open_count + 1, close_count)
  if close_count < open_count:
    parens += parens4(n, partial + ")", open_count, close_count + 1)
  return parens

import unittest

class Test(unittest.TestCase):
  def test_parens1(self):
    self.assertEqual(parens1(1), ["()"])
    self.assertEqual(parens1(2), ["()()", "(())"])
    self.assertEqual(parens1(3), ["()()()", "()(())", "(())()", "(()())",
        "((()))"])
  
  def test_parens2(self):
    self.assertEqual(parens2(1), ["()"])
    self.assertEqual(parens2(2), ["(())", "()()"])
    self.assertEqual(parens2(3), ["((()))", "(()())", "(())()", "()(())",
        "()()()"])
    self.assertEqual(set(parens1(7)), set(parens2(7)))
  
  def test_parens3(self):
    self.assertEqual(parens3(1), ["()"])
    self.assertEqual(parens3(2), ["(())", "()()"])
    self.assertEqual(parens3(3), ["((()))", "(()())", "(())()", "()(())",
        "()()()"])
    self.assertEqual(set(parens1(7)), set(parens3(7)))

  def test_parens4(self):
    self.assertEqual(parens4(1), ["()"])
    self.assertEqual(parens4(2), ["(())", "()()"])
    self.assertEqual(parens4(3), ["((()))", "(()())", "(())()", "()(())",
        "()()()"])
    self.assertEqual(set(parens1(7)), set(parens4(7)))

if __name__ == "__main__":
  unittest.main()

