# Determine whether or not one string is a permutation of another.

def is_permutation(str1, str2):
  counter = Counter()
  for letter in str1:
    counter[letter] += 1
  for letter in str2:
    if not letter in counter:
      return False
    counter[letter] -= 1
    if counter[letter] == 0:
      del counter[letter]
  return len(counter) == 0

class Counter(dict):
  def __missing__(self, key):
    return 0

if __name__ == "__main__":
  import sys
  print(is_permutation(sys.argv[-2], sys.argv[-1]))
