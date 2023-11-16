import unittest
from katas import ip_validation

class IpValidationTest(unittest.TestCase):
    def test_valid_ips(self):
        self.assertTrue(ip_validation.is_valid_IP('12.255.56.1'))
        self.assertTrue(ip_validation.is_valid_IP('127.1.1.0'))
        self.assertTrue(ip_validation.is_valid_IP('0.0.0.0'))
        self.assertTrue(ip_validation.is_valid_IP('0.34.82.53'))

    def test_empty_string(self):
        self.assertFalse(ip_validation.is_valid_IP(''))

    def test_letters(self):
        self.assertFalse(ip_validation.is_valid_IP('abc.def.ghi.jkl'))

    def test_wrong_numbers(self):
        self.assertFalse(ip_validation.is_valid_IP('123.456.789.0'))
        self.assertFalse(ip_validation.is_valid_IP('123.045.067.089'))
        self.assertFalse(ip_validation.is_valid_IP('192.168.1.300'))
        self.assertFalse(ip_validation.is_valid_IP('12.34.56.-1'))

    def test_format(self):
        self.assertFalse(ip_validation.is_valid_IP('213..116.154'))
        self.assertFalse(ip_validation.is_valid_IP('12.34.56'))
        self.assertFalse(ip_validation.is_valid_IP('12.34.56 .1'))
        
        

if __name__ == "__main__":
    unittest.main()



