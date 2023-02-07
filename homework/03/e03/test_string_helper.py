
import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
         # with assertEqual you can check if two values the same:
         self.assertEqual(is_name("Ville Virtanen"), True)

         # but if the function just returns True or False, it may be easier
         # to use assertTrue of assertFalse:

         # Add more tests in here!
         self.assertTrue(is_name("Ville Virtanen"))
         self.assertFalse(is_name("ville"))
         self.assertFalse(is_name("Ville"))
         self.assertFalse(is_name("jaakko Jaakkonen"))
         self.assertFalse(is_name("Jaakko jaakkonen"))
         self.assertTrue(is_name("Sami-Pekka Mäkelä-Käkelä"))