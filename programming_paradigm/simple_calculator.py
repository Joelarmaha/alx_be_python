# simple_calculator.py
class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), 5)
        self.assertEqual(self.calc.subtract(-1, 1), 0)
    def test_multiply(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.multiply(2, 3), 5)
        self.assertEqual(self.calc.multiply(-1, 1), 0)
    def test_divide(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.divide(2, 3), 5)
        self.assertEqual(self.calc.divide(-1, 1), 0)
