import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self): 
        self.assertRaises(Exception, is_name, 2222222)
        self.assertRaises(Exception, is_name, True)

        self.assertFalse(is_name("Jar1 Saarinen"))
        self.assertFalse(is_name("Jari Saar1nen"))
        self.assertFalse(is_name("    Saarinen"))
        self.assertFalse(is_name("jari Saarinen"))
        self.assertFalse(is_name("Jari saarinen"))

        self.assertTrue(is_name("Jari Saarinen"))

    def list_to_str(self):
        self.assertRaises(Exception, list_to_str, 2222)
        self.assertRaises(Exception, list_to_str, ["", " "])
        self.assertRaises(Exception, list_to_str, [1, True])

        self.assertEqual(list_to_str([]), "Empty List\n")
        test_array = ["hello", "hi"]
        self.assertEqual(list_to_str(test_array)[:9], "Database")