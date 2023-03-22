import unittest
from katas import human_time

class MakeReadableTest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(human_time.make_readable(0), "00:00:00")
        self.assertEqual(human_time.make_readable(5), "00:00:05")
        self.assertEqual(human_time.make_readable(60), "00:01:00")
        self.assertEqual(human_time.make_readable(86399), "23:59:59")
        self.assertEqual(human_time.make_readable(359999), "99:59:59")
