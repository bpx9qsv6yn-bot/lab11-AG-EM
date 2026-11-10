# https://github.com/EshuMarneedi/lab11-EM-AG
# Partner 1: Eshan Marneedi
# Partner 2: Ansh Gupta

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(10, add(5,5))

    def test_subtract(self): # 3 assertions
        self.assertEqual(1, sub(2,1))

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(6, multiply(2,3))
        self.assertEqual(-6, multiply(-2,3))
        self.assertEqual(0, multiply(0,5))

    def test_divide(self): # 3 assertions
        # divide(a, b) returns b / a
        self.assertEqual(5, divide(2,10))
        self.assertEqual(-2, divide(-4,8))
        self.assertEqual(0.5, divide(4,2))
    ##########################

    def test_divide_by_zero(self): # 1 assertion
        self.assertIsNone(divide(0,1))

    def test_logarithm(self): # 3 assertions
        # log(a, b) returns log base b of a
        self.assertEqual(2, log(4,2))
    def test_log_invalid_base(self): # 1 assertion
        self.assertIsNone(log(5,0))
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # logarithm catches its own ValueError and returns None
        self.assertIsNone(logarithm(0,5))

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5, hypotenuse(3,4))
        self.assertEqual(13, hypotenuse(5,12))
        self.assertEqual(7, hypotenuse(0,7))

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument
        self.assertIsNone(square_root(-1))
        # Test basic function
        self.assertEqual(3, square_root(9))
        self.assertEqual(1.5, square_root(2.25))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()