import unittest
import string_utils
class TestStringUtils(unittest.TestCase):
  def test_reverse_string(self):
    self.assertEqual(string_utils.reverse_string("mochi"), "ihcom")
 
  def test_capitalize_string(self):
    self.assertEqual(string_utils.capitalize_string("mochi telli"), "Mochi telli")
    self.assertEqual(string_utils.capitalize_string("mochi Telli"), "Mochi telli") 
    self.assertEqual(string_utils.capitalize_string("Mochi telli"), "Mochi telli")
    self.assertEqual(string_utils.capitalize_string("Mochi Telli"), "Mochi telli")
 
  def test_is_capitalized(self):
    self.assertTrue(string_utils.is_capitalized("Mochi Telli"))
    self.assertTrue(string_utils.is_capitalized("Mochi telli"))
    self.assertFalse(string_utils.is_capitalized("mochi Telli"))
    self.assertFalse(string_utils.is_capitalized("mochi telli"))
  

if __name__ == "__main__":
  unittest.main()
