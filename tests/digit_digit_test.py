import unittest

from katas import digit_digit

class DigitDigitTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(digit_digit.square(0), 0)

    def test_second(self):
        self.assertEqual(digit_digit.square(9119), 811181)

    def test_third(self):
        self.assertEqual(digit_digit.square(765), 493625)

if __name__ == '__main__':
    unittest.main()
