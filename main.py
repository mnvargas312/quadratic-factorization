from utils.parser import parse_quadratic
from utils.gcf import find_gcf
from utils.factorization import (
    calculate_factors,
    find_pair_with_sum,
    simplify_fraction,
)
from models.quadratic import QuadraticEquation

def main():
    # Step 1: Get input from the user (e.g., "2x^2 + 4x - 6")
    user_input = input("Enter a quadratic equation: ")

    # Step 2: Parse the input and create a QuadraticEquation object
    quadratic = parse_quadratic(user_input)

    # Step 3: Find the GCF of A, B, and C
    gcf = find_gcf(quadratic)

    # Step 4: Calculate factors of A * C
    factors = calculate_factors(quadratic.a, quadratic.c)

    # Step 5: Find the pair of factors whose sum equals B
    factor_pair = find_pair_with_sum(factors, quadratic.b)

    # Step 6: Simplify the fractions for each factor
    first_fraction = simplify_fraction(factor_pair[0], quadratic.a)
    second_fraction = simplify_fraction(factor_pair[1], quadratic.a)

    # Step 7: Output the factors
    if gcf > 1:
        print(f"GCF: {gcf}")
    print(f"Factors: ({first_fraction})({second_fraction})")

if __name__ == "__main__":
    main()
