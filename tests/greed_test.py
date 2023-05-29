import unittest

from katas import greed

class GreedTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual( greed.score( [5, 1, 3, 4, 1] ),  250)
        self.assertEqual( greed.score( [1, 1, 1, 3, 1] ), 1100)
        self.assertEqual( greed.score( [2, 3, 4, 6, 2] ),    0)
        self.assertEqual( greed.score( [4, 4, 4, 3, 3] ),  400)
        self.assertEqual( greed.score( [2, 4, 4, 5, 4] ),  450)

if __name__ == '__main__':
    unittest.main()
