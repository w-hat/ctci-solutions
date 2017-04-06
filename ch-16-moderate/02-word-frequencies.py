# Report word frequencies for a text.

class TextStats(object):
  def __init__(self, lines):
    self.total_words = 0
    self.word_counts = Counter()
    for line in lines:
      words = line.strip().split(" ")
      self.total_words += len(words)
      for word in words:
        self.word_counts[word] += 1
  
  def word_frequency(self, word):
    if self.total_words == 0:
      return None
    return float(self.word_counts[word]) / self.total_words

class Counter(dict):
  def __missing__(self, item):
    return 0

import unittest

class Test(unittest.TestCase):
  def test_word_frequency(self):
    text = """
        When the sun shines, we'll shine together
        Told you I'd be here forever
        Said I'll always be a friend
        Took an oath I'ma stick it out 'til the end
        Now that it's raining more than ever
        Know that we'll still have each other
        You can stand under my umbrella
        You can stand under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh)
        Under my umbrella
        (Ella ella eh eh eh eh eh eh)"""
    stats = TextStats(text.strip().split("\n"))
    self.assertEqual(stats.total_words, 87)
    self.assertEqual(stats.word_frequency("umbrella"), 5 / 87.0)

if __name__ == "__main__":
  unittest.main()

