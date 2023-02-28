import unittest

from katas import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), 'Hello')

if __name__ == '__main__':
    unittest.main()
