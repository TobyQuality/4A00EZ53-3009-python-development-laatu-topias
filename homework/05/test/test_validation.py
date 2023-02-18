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

    def test_is_personal_id(self):
        self.assertTrue(is_personal_id("131052-308T"))
        self.assertTrue(is_personal_id("120464-121C"))
        self.assertTrue(is_personal_id("210668-677S"))
        self.assertTrue(is_personal_id("140100A4744"))

        self.assertFalse(is_personal_id("ABCDEFGHIJK"))
        self.assertFalse(is_personal_id("1111111111111"))
        self.assertFalse(is_personal_id("987654A1234"))
        self.assertFalse(is_personal_id("011600A123A"))
        self.assertFalse(is_personal_id("011131A256S"))
        self.assertFalse(is_personal_id("070595-9999"))
        #otherwise alright, but wrong check digit
        self.assertFalse(is_personal_id("111111A111B"))

        self.assertRaises(Exception, is_personal_id, 1111111111)

