# Determine whether or not a string is a permutation of a palindrome,
# ignoring spaces.

def is_palindrome_permutation(string):
  counter = Counter()
  for letter in string.replace(" ", ""):
    counter[letter] += 1
  #return sum([count % 2 for count in counter.values()]) < 2
  odd_counts = 0
  for count in counter.values():
    odd_counts += count % 2
    if odd_counts > 1:
      return False
  return True

class Counter(dict):
  def __missing__(self, key):
    return 0

if __name__ == "__main__":
  import sys
  print(is_palindrome_permutation(sys.argv[-1]))
