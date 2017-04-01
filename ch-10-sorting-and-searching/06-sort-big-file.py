# Sort a big file.

import os

ONE_GIGABYTE = 64

def sort_big_file(input_filename, output_filename):
  in_file = open(input_filename, "r")
  temp_files = [open("temp-0.txt", "w+")]
  index = 0
  next_line = in_file.readline()
  temp_size = 0
  while next_line:
    if temp_size + len(next_line) > ONE_GIGABYTE:
      temp_name = "temp-" + str(len(temp_files) + 1) + ".txt"
      temp_files.append(open(temp_name, "w+"))
      temp_size = 0
    temp_size += len(next_line)
    temp_files[-1].write(next_line)
    next_line = in_file.readline()
  min_heap = MinHeap()
  sorted_files = []
  for f in temp_files:
    f.close()
    sort_in_memory(f.name)
    sorted_file = open(f.name, "r")
    min_heap.add((sorted_file.readline(), sorted_file))
  out_file = open(output_filename, "w")
  next = min_heap.remove()
  while next:
    (next_line, f) = next
    out_file.write(next_line)
    line = f.readline()
    if line:
      min_heap.add((line, f))
    next = min_heap.remove()
  for f in temp_files:
    f.close()
    os.remove(f.name)

def sort_in_memory(small_filename):
  small_file = open(small_filename, "r")
  lines = small_file.readlines()
  small_file.close()
  small_file = open(small_filename, "w")
  lines.sort()
  small_file.writelines(lines)
  small_file.close()

class MinHeap(object):
  def __init__(self):
    self.data = [None]
  
  def add(self, item):
    self.data.append(item)
    ix = len(self.data) - 1
    while ix and (item < self.data[ix/2]):
      self.data[ix], self.data[ix/2] = self.data[ix/2], item
      ix /= 2
  
  def remove(self):
    if len(self.data) == 1:
      return None
    if len(self.data) == 2:
      return self.data.pop()
    minimum = self.data[1]
    self.data[1] = self.data.pop()
    ix = 1
    while 2*ix < len(self.data):
      child_ix = 2*ix
      if 2*ix+1 < len(self.data) and self.data[child_ix] > self.data[2*ix+1]:
        child_ix = 2*ix + 1
      if self.data[child_ix] >= self.data[ix]:
        break
      self.data[child_ix], self.data[ix] = self.data[ix], self.data[child_ix]
      ix = child_ix
    return minimum

import unittest

class Test(unittest.TestCase):
  def test_min_heap(self):
    mh = MinHeap()
    mh.add(27)
    mh.add(22)
    mh.add(20)
    mh.add(31)
    mh.add(35)
    mh.add(19)
    mh.add(30)
    mh.add(18)
    self.assertEqual(mh.remove(), 18)
    self.assertEqual(mh.remove(), 19)
    self.assertEqual(mh.remove(), 20)
    self.assertEqual(mh.remove(), 22)
    self.assertEqual(mh.remove(), 27)
    self.assertEqual(mh.remove(), 30)
    self.assertEqual(mh.remove(), 31)
    self.assertEqual(mh.remove(), 35)
  
  def test_sort_big_file(self):
    big_file = open("big-input-file.txt", "w")
    big_file.write("""Haskell
Golang
Erlang
Ruby
Chess
Arimaa
AlphaGo
Self-driving cars
Convolutional neural networks
TensorFlow
Fourier transform
Coq
CFDG
Processing
Art festival
Scrabble
Bananagrams
Frisbee
Basketball
Soccer
Tennis
Quantum computers
Encryption
Topology
Homotopy
Combinatorics
Generating functions
Matrix completion
""")
    ordered = """AlphaGo
Arimaa
Art festival
Bananagrams
Basketball
CFDG
Chess
Combinatorics
Convolutional neural networks
Coq
Encryption
Erlang
Fourier transform
Frisbee
Generating functions
Golang
Haskell
Homotopy
Matrix completion
Processing
Quantum computers
Ruby
Scrabble
Self-driving cars
Soccer
Tennis
TensorFlow
Topology
"""
    big_file.close()
    sort_big_file("big-input-file.txt", "big-output-file.txt")
    output_file = open("big-output-file.txt", "r")
    self.assertEqual("".join(output_file.readlines()), ordered)
    output_file.close()
    os.remove("big-output-file.txt")
    os.remove("big-input-file.txt")

if __name__ == "__main__":
  unittest.main()

