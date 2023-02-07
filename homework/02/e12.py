import unittest

"""
This method sums up two digits
"""
def calculate_sum(a, b):
    return a + b

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        #self.assertEqual("hello", "hello")
        #self.assertEqual("hello", "world")
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)