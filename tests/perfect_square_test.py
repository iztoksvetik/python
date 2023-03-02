import unittest

from katas import perfect_square

class PerfectSquareTest(unittest.TestCase):
    def test_not_square(self):
        self.assertEqual(perfect_square.next(114), -1)

    def test_finds_next(self):
        self.assertEqual(perfect_square.next(121), 144)
        self.assertEqual(perfect_square.next(625), 676)

if __name__ == '__main__':
    unittest.main()


