# Group string anagrams together.

def group_anagrams(strings):
  pairs = [(s, sorted(s)) for s in strings]
  pairs.sort(key=lambda p: p[1])
  return [p[0] for p in pairs]

import unittest

class Test(unittest.TestCase):
  def test_group_anagrams(self):
    strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
    self.assertEqual(group_anagrams(strings),
              ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"])

if __name__ == "__main__":
  unittest.main()

