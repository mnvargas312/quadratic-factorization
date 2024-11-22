import unittest
from utils.parser import parse_quadratic
from models.quadratic import QuadraticEquation

class TestParser(unittest.TestCase):
    def test_valid_quadratic(self):
        """
        Test that valid quadratic equations are parsed correctly.
        """

    def test_no_constant_term(self):
        """
        Test parsing a quadratic equation without a constant term.
        """

    def test_missing_x_term(self):
        """
        Test parsing a quadratic equation without an x term.
        """

    def test_negative_coefficients(self):
        """
        Test parsing quadratic equations with negative coefficients.
        """

    def test_invalid_input(self):
        """
        Test parsing invalid input (e.g., not a quadratic equation).
        """

if __name__ == "__main__":
    unittest.main()
