# Determine whether the edit distance between two strings is less than 2.

def one_away(str1, str2):
  len_diff = abs(len(str1) - len(str2))
  if len_diff > 1:
    return False
  elif len_diff == 0:
    difference_count = 0
    for i in xrange(len(str1)):
      if str1[i] != str2[i]:
        difference_count += 1
        if difference_count > 1:
          return False
    return True
  else:
    if len(str1) > len(str2):
      longer, shorter = str1, str2
    else:
      longer, shorter = str2, str1
    shift = 0
    for i in xrange(len(shorter)):
      if shorter[i] != longer[i + shift]:
        if shift or (shorter[i] != longer[i + 1]):
          return False
        shift = 1
    return True

if __name__ == "__main__":
  import sys
  print(one_away(sys.argv[-2], sys.argv[-1]))
