import unittest

from katas import digital_root

class DigitalRootTest(unittest.TestCase):
    def test_is_seven(self):
        self.assertEqual(digital_root.get(16), 7)

    def test_is_six(self):
        self.assertEqual(digital_root.get(942), 6)

    def test_is_also_six(self):
        self.assertEqual(digital_root.get(132189), 6)

    def test_is_two(self):
        self.assertEqual(digital_root.get(493193), 2)

if __name__ == '__main__':
    unittest.main
