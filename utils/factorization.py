import math

def calculate_factors(a, c):
	"""
	Calculate all factor pairs of A * C.

	Args:
			a (int): Coefficient of x^2.
			c (int): Constant term.

	Returns:
			list[list[int]]: A 2D list of factor pairs.
	"""
	# Calculate the product A * C
	product = a * c

	# Handle edge case: product is zero
	if product == 0:
		raise ValueError("Product of A and C cannot be zero.")
	
	# Initalize list
	factor_pairs = []

	# Loop through divisors up to square root of the absolute product
	for i in range(1, int(math.sqrt(abs(product))) + 1):
		if product % i == 0:  # Check if i is a factor of the product
			# Add both positive and negative pairs
			factor_pairs.append([i, product // i])
			factor_pairs.append([-i, -(product // i)])

	return factor_pairs

def find_pair_with_sum(factors, target_sum):
		"""
		Find the pair of factors whose sum equals the target (B).
		"""
		# TODO: Implement logic to find the correct factor pair
		for factor_pair in factors:
				if sum(factor_pair) == target_sum:
						return factor_pair
		return None

def simplify_fraction(numerator, denominator):
		"""
		Simplify a fraction and return the simplified numerator and denominator.
		"""
		# TODO: Implement fraction simplification logic
		from math import gcd
		g = gcd(numerator, denominator)
		return numerator // g, denominator // g