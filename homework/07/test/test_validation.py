import unittest
from validation import *

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