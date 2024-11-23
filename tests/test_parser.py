import unittest
from utils.parser import (parse_quadratic, parse_coefficient)
from models.quadratic import QuadraticEquation

class TestParser(unittest.TestCase):
	def test_implicit_positive(self):
		"""Test implicit positive coefficient (empty or '+')."""
		self.assertEqual(parse_coefficient(""), 1)
		self.assertEqual(parse_coefficient("+"), 1)
	
	def test_implicit_negative(self):
		"""Test implicit negative coefficient ('-')."""
		self.assertEqual(parse_coefficient("-"), -1)

	def test_explicit_positive(self):
		"""Test explicit positive coefficients."""
		self.assertEqual(parse_coefficient("2"), 2)
		self.assertEqual(parse_coefficient("+3"), 3)

	def test_explicit_negative(self):
		"""Test explicit negative coefficients."""
		self.assertEqual(parse_coefficient("-2"), -2)
		self.assertEqual(parse_coefficient("-4"), -4)

	def test_invalid_inputs(self):
		"""Test invalid inputs raise a ValueError."""
		with self.assertRaises(ValueError):
			parse_coefficient("abc")
		with self.assertRaises(ValueError):
			parse_coefficient("3.5")  # Optional: Only integers are valid
		with self.assertRaises(ValueError):
			parse_coefficient("++")
		with self.assertRaises(ValueError):
			parse_coefficient("--")
	
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
		input_eq = "x^2 + 3x"
		expected = QuadraticEquation(1, 3, 0)
		result = parse_quadratic(input_eq)

		self.assertEqual(result.get_a(), expected.get_a())
		self.assertEqual(result.get_b(), expected.get_b())
		self.assertEqual(result.get_c(), expected.get_c())

	def test_missing_x_term(self):
		"""
		Test parsing a quadratic equation without an x term.
		"""
		input_eq = "-3x^2 +3"
		expected = QuadraticEquation(-3, 0, 3)
		result = parse_quadratic(input_eq)

		self.assertEqual(result.get_a(), expected.get_a())
		self.assertEqual(result.get_b(), expected.get_b())
		self.assertEqual(result.get_c(), expected.get_c())

	def test_negative_coefficients(self):
		"""
		Test parsing quadratic equations with negative coefficients.
		"""
		input_eq = "-2x^2 -3x -8"
		expected = QuadraticEquation(-2, -3, -8)
		result = parse_quadratic(input_eq)

		self.assertEqual(result.get_a(), expected.get_a())
		self.assertEqual(result.get_b(), expected.get_b())
		self.assertEqual(result.get_c(), expected.get_c())

	def test_invalid_input(self):
		"""
		Test parsing invalid input (e.g., not a quadratic equation).
		"""

if __name__ == "__main__":
	unittest.main()
