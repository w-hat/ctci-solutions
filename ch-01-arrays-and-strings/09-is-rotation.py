# Determine whether or not a given string is a rotation of another string.

import unittest

def is_rotation(s1, s2):
  if len(s1) != len(s2):
    return False
  return is_substring(s1 + s1, s2)
  
def is_substring(s1, s2):
  if len(s2) > len(s1):
    return False
  for i in xrange(len(s1) - len(s2) + 1):
    is_substring_here = True
    for j in xrange(len(s2)):
      if s1[i + j] != s2[j]:
        is_substring_here = False
        break
    if is_substring_here:
      return True
  return False

class Test(unittest.TestCase):
  def test_is_rotation(self):
    s1 = "tabletop"
    s2 = "toptable"
    s3 = "optalbet"
    self.assertTrue(is_rotation(s1, s2))
    self.assertFalse(is_rotation(s1, s3))
  
  def test_is_substring(self):
    s1 = "cat in the hat"
    s2 = "cat"
    s3 = "hat"
    s4 = "cats"
    self.assertTrue(is_substring(s1, s2))
    self.assertTrue(is_substring(s1, s3))
    self.assertFalse(is_substring(s1, s4))

if __name__ == "__main__":
  unittest.main()
