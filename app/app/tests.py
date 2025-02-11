"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add(self):
        """Test adding two numbers"""
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract(self):
        """Test subtracting two numbers"""
        self.assertEqual(calc.subtract(5, 11), 6)
