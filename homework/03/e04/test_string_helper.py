
import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # returns True
        self.assertTrue(is_name("ville virtanen", ignore_case=True))

        # returns False
        self.assertFalse(is_name("ville virtanen", ignore_case=False))

        # returns True
        self.assertTrue(is_name("Ville Virtanen", ignore_case=False) )

        # returns True
        self.assertTrue(is_name("Ville Virtanen"))

        # returns False
        self.assertFalse(is_name("ville virtanen"))
