import unittest
from katas import odd_int

class OddIntTest(unittest.TestCase):
    def test_single(self):
        self.assertEqual(odd_int.find_it([0]), 0)
        self.assertEqual(odd_int.find_it([7]), 7)

    def test_complex(self):
        self.assertEqual(odd_int.find_it([1,1,2]), 2)
        self.assertEqual(odd_int.find_it([0,1,0,1,0]), 0)
        self.assertEqual(odd_int.find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]), 4)
        self.assertEqual(odd_int.find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

if __name__ == '__main__':
    unittest.main()


