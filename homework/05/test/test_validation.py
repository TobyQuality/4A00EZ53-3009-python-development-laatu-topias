import unittest

from util.validation import *
# from util.validation import is_email
# from util.validation import is_personal_id

class TestValidation(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("2022-10-10"))
        self.assertTrue(is_date("2022-01-01"))
        self.assertTrue(is_date("2022-12-31"))
        self.assertTrue(is_date("2020-02-29"))
        self.assertTrue(is_date("0-01-21"))
        self.assertTrue(is_date("199-9-8"))

        self.assertFalse(is_date("2020-04-31"))
        self.assertFalse(is_date("2020-20-31"))
        self.assertFalse(is_date("2020-01-40"))
        self.assertFalse(is_date("2020-*1-30"))
        self.assertFalse(is_date("01-01-2022"))
        self.assertFalse(is_date("12-31-2022"))
        self.assertFalse(is_date("2022,12,31"))
        self.assertFalse(is_date("20221231"))
        self.assertFalse(is_date("1900-02-29"))

        self.assertRaises(Exception, is_date, 2022-31-12)
        self.assertRaises(Exception, is_date, 20223112)
    
    def test_is_date(self):
        self.assertTrue(is_email("jussi.pohjolainen@tuni.fi"))
        self.assertTrue(is_email("heh@gmail.com"))
        self.assertTrue(is_email("Ep1c-H4xx0rz@gmail.com"))

        self.assertFalse(is_email("jaakko.jaakkonen@.fi"))
        self.assertFalse(is_email("jaakko..jaakkonen@gmail.com"))
        self.assertFalse(is_email(".jaakko.jaakkonen@gmail.com"))
        self.assertFalse(is_email("jaakko.jaakkonen.@gmail.com"))
        self.assertFalse(is_email("jaakko jaakkonen.@gmail.com"))
        self.assertFalse(is_email("@gmail.com"))
        self.assertFalse(is_email("jaakko.jaakkonengmail.com"))
        self.assertFalse(is_email("jaakko.jaakkonen@.com"))
        self.assertFalse(is_email("jaakko.jaakkonen@com"))
        self.assertFalse(is_email("jaakko.jaakkonen@gmail."))
        self.assertFalse(is_email("     @gmail.com"))
        self.assertFalse(is_email("*^@gmail.com"))

        self.assertRaises(Exception, is_email, 666)
