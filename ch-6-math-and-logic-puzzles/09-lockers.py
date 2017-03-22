# How many lockers are left open if each locker is toggles once for each of
# its divisors.

import math

# Lemma 1: If p^{q} is prime power, then p^{2q} has an odd number of divisors.
# Proof:   All of the divisors of p^{2q} are {1, p, p^2, ..., p^{2q}} which 
#          has odd cardinality.

# Lemma 2: Let n^2 be a square number.  Then n has an odd number of divisors.
# Proof:   For a base case, notice that 1 has an odd number of divisors.
#          Now, suppose that m^2 has an odd number of divisors.  Then the
#          number of divisors of (m * p^q)^2 is the product of tow odd numbers
#          for any power of primes p^q.  This completes the proof by induction
#          on the prime power factors of n^2.

# Theorem: The number n has an odd number of divisors if and only if n is a 
#          square number.
# Proof:   Suppose n is not a square number.  Then n= p^q * m where q is odd
#          and m is not divisible by p.  Then n has an even number of divisors. 

def lockers_left_open(n):
  return int(math.sqrt(n-1))

import unittest

class Test(unittest.TestCase):
  def test_lockers_left_open(self):
    self.assertEqual(lockers_left_open(100), 9)
    self.assertEqual(lockers_left_open(200), 14)

if __name__ == "__main__":
  unittest.main()

