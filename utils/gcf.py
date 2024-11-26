from math import gcd
from functools import reduce

def find_gcf(a, b, c):
    """
    Find the greatest common factor (GCF) of the coefficients A, B, and C.
    If A is negative, the GCF will also be negative.

    Args:
        a (int): Coefficient of x^2.
        b (int): Coefficient of x.
        c (int): Constant term.

    Returns:
        int: The GCF of the coefficients A, B, and C.
    """
    # Handle edge case: if all coefficients are zero
    if a == 0 and b == 0 and c == 0:
        raise ValueError("Cannot calculate GCF for all zero coefficients.")

    # Calculate the GCF of all coefficients
    gcf = reduce(gcd, [a, b, c])

    # If the leading coefficient (a) is negative, make the GCF negative
    if a < 0:
        gcf = -gcf

    return gcf
