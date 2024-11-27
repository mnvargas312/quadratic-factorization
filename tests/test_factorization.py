import unittest
from utils.factorization import calculate_factors

class TestCalculateFactors(unittest.TestCase):

    def test_positive_product(self):
        """Test factor pairs for a positive product."""
        self.assertEqual(
            calculate_factors(2, 12),
            [[1, 24], [-1, -24], [2, 12], [-2, -12], [3, 8], [-3, -8], [4, 6], [-4, -6]]
        )

    def test_negative_product(self):
        """Test factor pairs for a negative product."""
        self.assertEqual(
            calculate_factors(2, -12),
            [[1, -24], [-1, 24], [2, -12], [-2, 12], [3, -8], [-3, 8], [4, -6], [-4, 6]]
        )

    def test_prime_product(self):
        """Test factor pairs for a prime product."""
        self.assertEqual(
            calculate_factors(1, 13),
            [[1, 13], [-1, -13]]
        )

    def test_zero_product(self):
        """Test factor pairs when the product is zero."""
        with self.assertRaises(ValueError):
            calculate_factors(0, 12)

if __name__ == "__main__":
    unittest.main()
