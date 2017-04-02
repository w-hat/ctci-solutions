# Design an in-memory file system.

class Directory(object):
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.files = {}
    self.subdirectories = {}
  
  def addDirectory(self, directory):
    if directory.parent:
      del directory.parent.subdirectories[directory.name]
    directory.parent = self
    self.subdirectories[directory.name] = directory
  
  def addFile(self, file):
    self.files[file.name] = file
  
  def get(self, path):
    parts = path.split("/")
    directory = self
    for part in parts:
      if part == '..':
        directory = directory.parent
        if not directory:
          return None
      elif part in directory.subdirectories:
        directory = directory.subdirectories[part]
      elif part in directory.files:
        return directory.files[part]
      else:
        return None
    return directory
  
class File(object):
  def __init__(self, name, content):
    self.name, self.content = name, content

class NoneHash(dict):
  def __missing__(self, item):
    return None

import unittest

class Test(unittest.TestCase):
  def test_directory(self):
    directory0 = Directory("root")
    directory1 = Directory("food")
    directory2 = Directory("vegetables")
    file1 = File("arugula.png", "345235434565")
    directory0.addDirectory(directory1)
    directory1.addDirectory(directory2)
    directory2.addFile(file1)
    self.assertEqual(directory0.get("food/vegetables/rutabaga.png"), None)
    self.assertEqual(directory0.get("food/vegetables/arugula.png"), file1)
    self.assertEqual(directory0.get(".."), None)
    self.assertEqual(directory2.get(".."), directory1)

if __name__ == "__main__":
  unittest.main()

