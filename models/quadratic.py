class QuadraticEquation:
	def __init__(self, a, b, c):
		"""
		Initialize a QuadraticEquation object.

		Args:
		- a (int or float): Coefficient of x^2
		- b (int or float): Coefficient of x
		- c (int or float): Constant term
		"""
		self._a = None
		self._b = None
		self._c = None

		self.set_a(a)  # Use setter to enforce validation
		self.set_b(b)
		self.set_c(c)

	# Getter and Setter for 'a'
	def get_a(self):
		return self._a

	def set_a(self, value):
		if value == 0:
			raise ValueError("Coefficient 'a' cannot be 0 for a quadratic equation.")
		self._a = value

	# Getter and Setter for 'b'
	def get_b(self):
		return self._b

	def set_b(self, value):
		self._b = value

	# Getter and Setter for 'c'
	def get_c(self):
		return self._c

	def set_c(self, value):
		self._c = value

	# Method to represent the quadratic equation as a string
	def __repr__(self):
		return f"{self._a}x^2 + {self._b}x + {self._c}"
