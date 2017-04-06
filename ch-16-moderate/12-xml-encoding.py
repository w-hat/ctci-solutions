# Encode some XML.

def xml_encoding(xml_object, mapping):
  parts = [str(mapping[xml_object.element])]
  for tag, value in sorted(xml_object.attributes.items(), reverse=True):
    parts.append(str(mapping[tag]))
    parts.append(str(value))
  parts.append("0")
  for child in xml_object.children:
    parts.append(xml_encoding(child, mapping))
  parts.append("0")
  return " ".join(parts)

class XMLObject(object):
  def __init__(self, element, attributes=None, children=None):
    self.element = element
    if attributes is None:
      self.attributes = {}
    else:
      self.attributes = attributes
    if children is None:
      self.children = []
    else:
      self.children = children

import unittest

class Test(unittest.TestCase):
  def test_xml_encoding(self):
    mapping = {"name": 1, "instrument": 2, "person": 3, "monkey": 4, "color": 5}
    xml = XMLObject("person",
        {"name": "The Man with the Yellow Hat", "instrument": "tuba"},
        [XMLObject("monkey", {"name": "George", "color": "brown"})])
    self.assertEqual(xml_encoding(xml, mapping),
        "3 1 The Man with the Yellow Hat 2 tuba 0 4 1 George 5 brown 0 0 0")

if __name__ == "__main__":
  unittest.main()

