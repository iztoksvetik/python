import unittest

from katas import phone_number

class PhoneNumberTest(unittest.TestCase):
    def test_formats_zeroes(self):
        self.assertEqual(phone_number.format([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

    def test_rising(self):
        self.assertEqual(phone_number.format([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), "(012) 345-6789")  

if __name__ == '__main__':
    unittest.main()

