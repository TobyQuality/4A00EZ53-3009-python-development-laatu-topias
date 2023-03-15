import unittest

from string_helper import is_name, get_title

class TestStringHelper(unittest.TestCase):
    def test_get_title(self): 
        test_title1 = """
        ------------------------------
        -         Battleship         -
        ------------------------------
        """.strip() # strip() will remove extra enters (\n) from start and end.

        self.assertEqual(get_title("Battleship", 30, "-"), test_title1)

        test_title2= """

        ****************************************
        *            Palindrome App            *
        ****************************************
        """.strip()

        self.assertEqual(get_title("Palindrome App", 40, "*"), test_title2)

        test_title3 = "invalid values, title length is > graph length"

        self.assertEqual(get_title("leisure suit larry",5, '-'), test_title3)