# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Tests for addition
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -1), -2)
        
    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        
    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    # Tests for subtraction
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        
    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        
    def test_subtract_bigger_from_smaller(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)
        
    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    # Tests for multiplication
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        
    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        
    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.2), 0.1, places=7)

    # Tests for division
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        
    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        
    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)
        
    def test_divide_floats(self):
        # Note: floating point division may have precision issues; test with almostEqual
        self.assertAlmostEqual(self.calc.divide(0.3, 0.1), 3.0, places=7)

if __name__ == '__main__':
    unittest.main()