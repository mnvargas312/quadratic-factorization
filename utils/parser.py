import re
from models.quadratic import QuadraticEquation

def parse_quadratic(equation_str):
	"""
	Parse a string representation of a quadratic equation and return
	a QuadraticEquation object.

	Args:
	- equation_str (str): The quadratic equation as a string, e.g., "2x^2 + 4x - 6".

	Returns:
	- QuadraticEquation: An object with coefficients a, b, and c.

	Raises:
	- ValueError: If the input string is not a valid quadratic equation.
	"""
	# Remove spaces from string
	equation_str = equation_str.replace (" ", "")

	terms = re.findall(r'[+-]?[^+-]+', equation_str)

	
	# Extract coefficents
	a, b, c = 0, 0, 0

	# Process each term
	for term in terms:
		if "x^2" in term:  # Quadratic term
			coefficient = term.replace("x^2", "")
			a = parse_coefficient(coefficient)
		elif "x" in term:  # Linear term
			coefficient = term.replace("x", "")
			b = parse_coefficient(coefficient)
		else:  # Constant term
			c = int(term)  # Constants are always integers

	print(f"Parsed coefficients: a={a}, b={b}, c={c}")

	# Return the parsed coefficients as a QuadraticEquation object
	return QuadraticEquation(a, b, c)

def parse_coefficient(coefficient_str):
    """
    Parse the coefficient of a term, handling implicit coefficients.

    Args:
        coefficient_str (str): The coefficient part of a term, e.g., "-3" or "".

    Returns:
        int: The parsed coefficient.
    """
    if coefficient_str == "" or coefficient_str == "+":
        return 1
    elif coefficient_str == "-":
        return -1
    else:
        return int(coefficient_str)