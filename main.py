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
    a, b, c = quadratic.get_a(), quadratic.get_b(), quadratic.get_c()
    gcf = find_gcf(a, b, c)

    # Step 4: Calculate factors of A * C
    factors = calculate_factors(a//gcf, c//gcf)

    # Step 5: Find the pair of factors whose sum equals B
    factor_pair = find_pair_with_sum(factors, b//gcf)

    # Step 6: Simplify the fractions for each factor
    first_fraction = simplify_fraction(factor_pair[0], a//gcf)
    second_fraction = simplify_fraction(factor_pair[1], a//gcf)

    # Step 7: Output the factors
    if gcf > 1:
        print(f"GCF: {gcf}")
    print(f"Factors: ({first_fraction})({second_fraction})")

if __name__ == "__main__":
    main()
