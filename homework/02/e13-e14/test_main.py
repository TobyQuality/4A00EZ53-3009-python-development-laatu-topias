import unittest

from main import calculate_sum, get_max, is_palindrome, reverse

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)

    def test_get_max(self):
        self.assertEqual(get_max(1, 2, 3), 3)
        self.assertEqual(get_max(100, 99, 98), 100)
        self.assertEqual(get_max(99, 101, 98), 101)
        self.assertEqual(get_max(-100, -98, -99), -98)
        self.assertEqual(get_max('a', 'b', 'c'), 'c')

    def test_reverse(self):
        self.assertEqual(reverse("apina"), "anipa")
        self.assertEqual(reverse("Moi"), "ioM")
        self.assertEqual(reverse("123"), "321")
    
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("Saippuakauppias", lowercase=True), True)
        self.assertEqual(is_palindrome("Saippuakauppias", lowercase=False), False)
        self.assertEqual(is_palindrome("Kalle", lowercase=False), False)