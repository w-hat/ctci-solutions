# Return the number of ways that an expression can be parenthesized and
# achieve a given truth value

def count_eval(expr, value, memo=None):
  if len(expr) % 2 == 0:
    return Exception("Malformed expression.")
  if len(expr) == 1:
    return int((expr == "0") ^ value)
  if memo is None:
    memo = {}
  elif expr in memo:
    counts = memo[expr]
    return counts[int(value)]
  true_count = 0
  for opix in xrange(1, len(expr) - 1, 2):
    left, op, right = expr[:opix], expr[opix], expr[(opix+1):]
    if op == '&':
      true_count += count_eval(left,True, memo) * count_eval(right,True, memo)
    elif op == '|':
      true_count += count_eval(left,True, memo) * count_eval(right,True, memo)
      true_count += count_eval(left,False,memo) * count_eval(right,True, memo)
      true_count += count_eval(left,True, memo) * count_eval(right,False,memo)
    elif op == '^':
      true_count += count_eval(left,True, memo) * count_eval(right,False,memo)
      true_count += count_eval(left,False,memo) * count_eval(right,True, memo)
    else:
      return Exception('Unknown operation.')
  total_count = catalan_number((len(expr) - 1) / 2)
  false_count = total_count - true_count
  counts = (false_count, true_count)
  memo[expr] = counts
  return counts[int(value)]

def catalan_number(n):
  number = 1
  for i in xrange(n + 1, 2*n + 1):
    number *= i
  for i in xrange(1, n + 2):
    number /= i
  return number

import unittest

class Test(unittest.TestCase):
  def test_count_eval(self):
    self.assertEqual(count_eval("1", True), 1)
    self.assertEqual(count_eval("0", True), 0)
    self.assertEqual(count_eval("0", False), 1)
    self.assertEqual(count_eval("1&1", True), 1)
    self.assertEqual(count_eval("1|0", False), 0)
    self.assertEqual(count_eval("1^0", True), 1)
    self.assertEqual(count_eval("1&0&1", True), 0)
    self.assertEqual(count_eval("1|1^0", True), 2)
    self.assertEqual(count_eval("1^0|0|1", False), 2)
    self.assertEqual(count_eval("1^0|0|1", True), 3)
    self.assertEqual(count_eval("0&0&0&1^1|0", True), 10)

  def test_catalan_number(self):
    self.assertEqual(catalan_number(0), 1)
    self.assertEqual(catalan_number(1), 1)
    self.assertEqual(catalan_number(2), 2)
    self.assertEqual(catalan_number(3), 5)
    self.assertEqual(catalan_number(4), 14)
    self.assertEqual(catalan_number(5), 42)

if __name__ == "__main__":
  unittest.main()

