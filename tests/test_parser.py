import unittest
from utils.parser import parse_quadratic
from models.quadratic import QuadraticEquation

class TestParser(unittest.TestCase):
    def test_valid_quadratic(self):
        """
        Test that valid quadratic equations are parsed correctly.
        """
        inputEquation = "2x^2 + 4x - 6"
        expectedOutput = QuadraticEquation(a=2, b=4, c=6)

        result = parse_quadratic(inputEquation)
        self.assertEqual(result.a, expectedOutput.a)
        self.assertEqual(result.b, expectedOutput.b)
        self.assertEqual(result.c, expectedOutput.c)

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
