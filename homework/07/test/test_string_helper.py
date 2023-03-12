import unittest
from string_helper import *

class TestStringHelper(unittest.TestCase):
    def test_with_valid_csv(self):
        csv = "1,Jussi,Virtanen\n2,Pekka,Keinänen"
        expected_output = [['1', 'Jussi', 'Virtanen'], ['2', 'Pekka', 'Keinänen']]
        self.assertEqual(csv_to_list(csv), expected_output)

    def test_with_empty_csv(self):
        csv = ""
        expected_output = [[""]]
        self.assertEqual(csv_to_list(csv), expected_output)

    def test_with_invalid_type(self):
        csv = 123
        with self.assertRaises(Exception):
            csv_to_list(csv)

if __name__ == '__main__':
    unittest.main()