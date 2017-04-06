# Return an English reading of the given number.

SINGLE_DIGIT = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
TEENS = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen'}
TENS = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'}
LARGE_NUMBERS = ['thousand', 'million', 'billion', 'trillion', 'quadrillion']

def english_int(n):
  if n == 0:
    return "zero"
  parts = []
  hundreds = n % 1000
  if hundreds != 0:
    parts.append(english_int_hundreds(hundreds))
  added_and = False
  magnitude_index = 0
  n /= 1000
  while n:
    if len(parts) > 0 and not added_and:
      parts.append("and")
      added_and = True
    hundreds = n % 1000
    if hundreds:
      parts.append(LARGE_NUMBERS[magnitude_index])
      parts.append(english_int_hundreds(hundreds))
    magnitude_index += 1
    n /= 1000
  return " ".join(reversed(parts))
  

def english_int_hundreds(n):
  if n == 0:
    return ""
  parts = []
  tens_ones = n % 100
  if tens_ones < 10:
    if tens_ones > 0:
      parts.append(SINGLE_DIGIT[tens_ones])
  elif tens_ones < 20:
    parts.append(TEENS[tens_ones])
  else:
    ones = tens_ones % 10
    tens = tens_ones - ones
    if ones > 0:
      parts.append(SINGLE_DIGIT[ones])
    parts.append(TENS[tens])
  hundreds = n / 100
  if hundreds:
    if len(parts) > 0:
      parts.append("and")
    parts.append("hundred")
    parts.append(SINGLE_DIGIT[hundreds])
  return " ".join(reversed(parts))

import unittest

class Test(unittest.TestCase):
  def test_english_int(self):
    self.assertEqual(english_int(0), "zero")
    self.assertEqual(english_int(1), "one")
    self.assertEqual(english_int(8), "eight")
    self.assertEqual(english_int(15), "fifteen")
    self.assertEqual(english_int(92), "ninety two")
    self.assertEqual(english_int(113), "one hundred and thirteen")
    self.assertEqual(english_int(1001), "one thousand and one")
    self.assertEqual(english_int(2075), "two thousand and seventy five")
    self.assertEqual(english_int(20066), "twenty thousand and sixty six")
    self.assertEqual(english_int(500012), "five hundred thousand and twelve")
    self.assertEqual(english_int(950000), "nine hundred and fifty thousand")
    self.assertEqual(english_int(1000000), "one million")
    self.assertEqual(english_int(6000000000), "six billion")
    self.assertEqual(english_int(2006000001), "two billion six million and one")
    self.assertEqual(english_int(6020000000), "six billion and twenty million")
    self.assertEqual(english_int(3000000000042), "three trillion and forty two")

if __name__ == "__main__":
  unittest.main()

