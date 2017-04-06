# Determine whether the given string matches the given pattern of a's and b's.

def matches_pattern(string, pattern):
  if len(pattern) == 0:
    return len(string) == 0
  if len(string) == 0:
    return True
  pattern = normalize(pattern)
  a_count, b_count = 0, 0
  for letter in pattern:
    if letter == 'a':
      a_count += 1
    else:
      b_count += 1
  for a_len in xrange(1, len(string) / a_count + 1):
    letters_left = len(string) - a_count * a_len
    if b_count and letters_left % b_count == 0:
      a_val = string[:a_len]
      b_len = (len(string) - a_count * a_len) / b_count
      if b_len == 0:
        break
      matches = try_pattern(string, pattern, a_val, b_len)
      if matches:
        return True
    elif letters_left == 0:
      return try_pattern(string, pattern, string[:a_len], 0)
  return False

def try_pattern(string, pattern, a_val, b_len):
  a_len, b_val = len(a_val), None
  ix = len(a_val)
  for letter in pattern[1:]:
    if letter == 'a':
      if string[ix : ix + a_len] == a_val:
        ix += a_len
      else:
        return False
    elif b_val is None:
      b_val = string[ix : ix + b_len]
      ix += b_len
    elif string[ix : ix + b_len] == b_val:
      ix += b_len
    else:
      return False
  return True

def normalize(pattern):
  if pattern[0] == "a":
    return pattern
  inverted = []
  for letter in pattern:
    if letter == "a":
      inverted.append("b")
    else:
      inverted.append("a")
  return "".join(inverted)

import unittest

class Test(unittest.TestCase):
  def test_matches_pattern(self):
    self.assertTrue(matches_pattern("dogdogturtledog", "aaba"))
    self.assertTrue(matches_pattern("dogdogturtledog", "bbab"))
    self.assertTrue(matches_pattern("dogdogturtledogdog", "aabaa"))
    self.assertTrue(matches_pattern("dogdogturtledogdog", "aba"))
    self.assertTrue(matches_pattern("dogdogturtledogdo", "aba"))
    self.assertFalse(matches_pattern("dogdogturtledogdg", "aba"))
    self.assertTrue(matches_pattern("catcatbirdbird", "aabb"))
    self.assertFalse(matches_pattern("catcatcatbirdbird", "aabb"))
    self.assertTrue(matches_pattern("buffalobuffalobuffalobuffalo", "aaaa"))
    self.assertFalse(matches_pattern("buffalobuffalouffalobuffalo", "aaaa"))

if __name__ == "__main__":
  unittest.main()

