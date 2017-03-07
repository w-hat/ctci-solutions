# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.

def compress(string):
  if len(string) == 0:
    return string
  parts = []
  current_letter = string[0]
  current_count = 1
  for letter in string[1:]:
    if current_letter == letter:
      current_count += 1
    else:
      parts.append(current_letter + str(current_count))
      current_letter = letter
      current_count = 1
  parts.append(current_letter + str(current_count))
  compressed = "".join(parts)
  if len(compressed) < len(string):
    return compressed
  else:
    return string

if __name__ == "__main__":
  import sys
  print(compress(sys.argv[-1]))
