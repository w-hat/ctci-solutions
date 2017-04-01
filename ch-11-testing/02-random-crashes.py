# A program never crashes in the same place, but it is supposed to crash
# uniformly randomly.  Test that a sequence behaves randomly.

# Note that the randomness test implemented here is very weak.

# TODO Implement the algorithm in this paper instead:
# ftp://ftp.inf.ethz.ch/pub/crypto/publications/Maurer92a.pdf

import math

def how_random(sequence):
  bit_counts = [0] * 128
  for element in sequence:
    for bit_ix in xrange(64):
      bit = 1 << bit_ix
      if element & bit:
        bit_counts[bit_ix] += 1
      else:
        bit_counts[bit_ix + 64] += 1
  total = sum(bit_counts)
  average = total / 128.0
  square_divergence = sum([abs(c - average) for c in bit_counts])
  if not square_divergence:
    return 1
  return 1 / math.sqrt(square_divergence)

import random
import unittest

random.seed(0)

class Test(unittest.TestCase):
  def test_randomness(self):
    sequence0 = [i % 2 for i in xrange(10000)]
    randomness0 = how_random(sequence0)
    self.assertTrue(randomness0 > 0.0 and randomness0 < 0.1)
    
    sequence1 = [i % 1000 for i in xrange(10000)]
    randomness1 = how_random(sequence1)
    self.assertTrue(randomness0 < randomness1)
    
    sequence2 = [(i * 6007) % 50000 for i in xrange(10000)]
    randomness2 = how_random(sequence2)
    self.assertTrue(randomness1 < randomness2)

    sequence3 = [random.randint(1, (1 << 64) - 1) for _ in xrange(10000)]
    randomness3 = how_random(sequence3)
    self.assertTrue(randomness2 < randomness3)

if __name__ == "__main__":
  unittest.main()

