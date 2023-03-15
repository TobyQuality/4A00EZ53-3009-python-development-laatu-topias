import unittest

from string_helper import get_title

class TestStringHelper(unittest.TestCase):
    def test_get_title(self):
        # expect an exception if title's length is greater than amount's value
        self.assertRaises(Exception, get_title, "abc", 2, "*")
        # expect an exception if title is not string
        self.assertRaises(Exception, get_title, 11, 2, "*")
        # expect an exception if amount is not integer
        self.assertRaises(Exception, get_title, "abc", "abc", "*")
        # expect an exception if char is not string
        self.assertRaises(Exception, get_title, "abc", 2, False)
        # expect an exception if title's length is not greater than 1
        self.assertRaises(Exception, get_title, "a", 2, "*")
        # expect an exception if char's length greater than 1
        self.assertRaises(Exception, get_title, "abc", 20, "**")