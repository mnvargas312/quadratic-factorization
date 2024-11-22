from math import gcd
from functools import reduce

def find_gcf(quadratic):
    """
    Find the greatest common factor (GCF) of A, B, and C.
    """
    # TODO: Implement logic to calculate the GCF
    return reduce(gcd, [quadratic.a, quadratic.b, quadratic.c])
