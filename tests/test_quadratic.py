import unittest
from models.quadratic import QuadraticEquation

class TestQuadratic(unittest.TestCase):
    def test_initialization(self):
        """Test proper initialization with valid coefficients."""
        quad_eq = QuadraticEquation(2, 3, -4)
        self.assertEqual(quad_eq.get_a(), 2)
        self.assertEqual(quad_eq.get_b(), 3)
        self.assertEqual(quad_eq.get_c(), -4)

    def test_initialization_invalid_a(self):
        """Test that initialization raises ValueError if a = 0."""
        with self.assertRaises(ValueError):
            QuadraticEquation(0, 2, 3)

    def test_getters(self):
        """Test the getter methods for a, b, and c."""
        quad_eq = QuadraticEquation(1, -5, 6)
        self.assertEqual(quad_eq.get_a(), 1)
        self.assertEqual(quad_eq.get_b(), -5)
        self.assertEqual(quad_eq.get_c(), 6)

    def test_setters(self):
        """Test the setter methods for a, b, and c."""
        quad_eq = QuadraticEquation(3, 4, 5)

        # Set valid values
        quad_eq.set_a(10)
        quad_eq.set_b(-2)
        quad_eq.set_c(8)

        self.assertEqual(quad_eq.get_a(), 10)
        self.assertEqual(quad_eq.get_b(), -2)
        self.assertEqual(quad_eq.get_c(), 8)

    def test_set_a_invalid(self):
        """Test that set_a raises ValueError if a = 0."""
        quad_eq = QuadraticEquation(1, 2, 3)
        with self.assertRaises(ValueError):
            quad_eq.set_a(0)

    def test_repr(self):
        """Test the string representation of the quadratic equation."""
        quad_eq = QuadraticEquation(2, -3, 4)
        self.assertEqual(repr(quad_eq), "2x^2 + -3x + 4")

    def test_edge_cases(self):
        """Test edge cases such as large values and floating-point coefficients."""
        quad_eq = QuadraticEquation(1e6, -1e-6, 0.0)
        self.assertEqual(quad_eq.get_a(), 1e6)
        self.assertEqual(quad_eq.get_b(), -1e-6)
        self.assertEqual(quad_eq.get_c(), 0.0)

if __name__ == "__main__":
    unittest.main()