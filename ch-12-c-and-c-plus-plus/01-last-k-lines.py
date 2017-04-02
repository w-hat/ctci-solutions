# Read the last k lines of a file with C or C++.

import ctypes
import os
if not os.path.isfile("./lastklines.so"):
  print("Run `make`.")
lib = ctypes.cdll.LoadLibrary('./lastklines.so')

def read_last_lines(filename, k):
  lib.lastklines.restype = ctypes.c_char_p
  return lib.lastklines(ctypes.c_char_p(filename), ctypes.c_int(k))

import unittest

class Test(unittest.TestCase):
  def test_read_last_lines(self):
    file0 = open('test-file.txt', 'w')
    file0.write("""Gattaca
Big Fish
The Princess Bride
Hidden Figures
Fantastic Mr. Fox
Get Out
Her
Big Hero 6
Zootopia
WALL-E
Yes Man
Stand and Deliver
Garden State
The Sound of Music
Dead Poets Society
Captain Fantastic
I Origins
Life of Pi
Interstellar
Ex Machina""")
    file0.close()
    result = read_last_lines("test-file.txt", 5)
    self.assertEqual(result,
        "Captain Fantastic\nI Origins\nLife of Pi\nInterstellar\nEx Machina\n")
    os.remove(file0.name)

if __name__ == "__main__":
  unittest.main()

