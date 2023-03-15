import unittest

from main import get_first_index

class TestMain(unittest.TestCase):
    def get_first_index(self):
        self.assertEqual(get_first_index("Tee", "e"), 1)
        self.assertEqual(get_first_index("Tee", "t"), -1)
        self.assertEqual(get_first_index("Azkaban", "n"), 7)