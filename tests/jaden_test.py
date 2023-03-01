import unittest
from katas import jaden

class JadenTest(unittest.TestCase):
    def test_first_quote(self):
        quote = 'How can mirrors be real if our eyes aren\'t real'
        self.assertEqual(jaden.case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")

    def test_second_quote(self):
        quote = 'Wow, this is such a cool way of writing things... not!'
        self.assertEqual(jaden.case(quote), 'Wow, This Is Such A Cool Way Of Writing Things... Not!')
        
if __name__ == '__main__':
    unittest.main()

