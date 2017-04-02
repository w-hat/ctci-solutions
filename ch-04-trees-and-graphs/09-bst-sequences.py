# Enumerate all inserrtion sequences that could have led to the given BST.

def bst_sequences(bst):
  return bst_sequences_partial([], [bst])
  
def bst_sequences_partial(partial, subtrees):
  if not len(subtrees):
    return [partial]
  sequences = []
  for index, subtree in enumerate(subtrees):
    next_partial = partial + [subtree.data]
    next_subtrees = subtrees[:index] + subtrees[index+1:]
    if subtree.left:
      next_subtrees.append(subtree.left)
    if subtree.right:
      next_subtrees.append(subtree.right)
    sequences += bst_sequences_partial(next_partial, next_subtrees)
  return sequences

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
  
import unittest

class Test(unittest.TestCase):
  def test_bst_sequences(self):
    self.assertEqual(bst_sequences(Node(7,Node(4,Node(5)),Node(9))), [
      [7, 4, 9, 5],
      [7, 4, 5, 9],
      [7, 9, 4, 5]])
    self.assertEqual(bst_sequences(Node(7,Node(4,Node(5),Node(6)),Node(9))), [
      [7, 4, 9, 5, 6],
      [7, 4, 9, 6, 5],
      [7, 4, 5, 9, 6],
      [7, 4, 5, 6, 9],
      [7, 4, 6, 9, 5],
      [7, 4, 6, 5, 9],
      [7, 9, 4, 5, 6],
      [7, 9, 4, 6, 5]])

if __name__ == "__main__":
  unittest.main()

