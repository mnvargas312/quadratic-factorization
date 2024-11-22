def calculate_factors(a, c):
    """
    Calculate all factor pairs of A * C.
    Returns a 2D list of factor pairs.
    """
    # TODO: Implement logic to calculate factor pairs
    return [[1, a * c], [-1, -a * c], [2, (a * c) // 2], [-2, -(a * c) // 2]]

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
