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

	pattern = r'([+-]?\d*)x\^2|([+-]?\d*)x|([+-]?\d+)'
	matches = re.findall(pattern, equation_str)
	
	if not matches:
		raise ValueError("Invalid quadratic equation format")
	
	# Extract Coeffiecents
	a, b, c = 0, 0, 0
	
	for match in matches:
		if match[0]:
			a = int(match[0]) if match[0] not in ("", "+", "-") else (1 if match[0] != "-" else -1)
		elif match[1]:
			b = int(match[1]) if match[1] not in ("", "+", "-") else (1 if match[1] != "-" else -1)
		elif match[2]:
			c = int(match[2])

	# Return Quadratic Equation object
	return QuadraticEquation(a=a, b=b, c=c)