import unittest
from utils.parser import parse_quadratic
from models.quadratic import QuadraticEquation

class TestParser(unittest.TestCase):
	def test_valid_quadratic(self):
		"""
		Test that valid quadratic equations are parsed correctly.
		"""
		input_eq = "2x^2 + 4x - 6"
		expected_output = QuadraticEquation(2, 4, -6)
		
		result = parse_quadratic(input_eq)
		self.assertEqual(result.get_a(), expected_output.get_a())
		self.assertEqual(result.get_b(), expected_output.get_b())
		self.assertEqual(result.get_c(), expected_output.get_c())

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
