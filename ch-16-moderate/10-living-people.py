# Find the year with the most living people.

def most_living_people(people):
  if len(people) == 0:
    return None
  change = [0] * 102
  alive = 0
  max_alive = 0
  max_year = 0
  for person in people:
    change[person.birth_year - 1900] += 1
    if person.death_year:
      change[person.death_year - 1899] -= 1 
  for year in xrange(0, 101):
    alive += change[year]
    if alive > max_alive:
      max_alive = alive
      max_year = year
  return max_year + 1900

class P(object):
  def __init__(self, born, died=None):
    self.birth_year = born
    self.death_year = died

import unittest

class Test(unittest.TestCase):
  def test_most_living_people(self):
    people=[P(1907,1942),P(1909,1982),P(1933,1967),P(1912,1954),P(1980),P(1988)]
    self.assertEqual(most_living_people(people), 1933)

if __name__ == "__main__":
  unittest.main()

