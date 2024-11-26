import unittest
from models.quadratic import QuadraticEquation
from utils.gcf import find_gcf

class TestFindGCF(unittest.TestCase):
    def test_gcf_with_negative_a(self):
        """Test GCF when the leading coefficient (a) is negative."""
        self.assertEqual(find_gcf(-2, 18, 40), -2)

    def test_gcf_with_positive_a(self):
        """Test GCF when the leading coefficient (a) is positive."""
        self.assertEqual(find_gcf(4, 8, 12), 4)

    def test_gcf_no_common_factor(self):
        """Test GCF when there is no common factor greater than 1."""
        self.assertEqual(find_gcf(-7, 11, 13), -1)

    def test_gcf_with_zero_coefficient(self):
        """Test GCF when one or more coefficients are zero."""
        self.assertEqual(find_gcf(-6, 0, 12), -6)

    def test_gcf_with_all_zeros(self):
        """Test GCF when all coefficients are zero."""
        with self.assertRaises(ValueError):
            find_gcf(0, 0, 0)

if __name__ == "__main__":
    unittest.main()