class QuadraticEquation:
    def __init__(self, a, b, c):
        """
        Initialize a QuadraticEquation object.

        Args:
        - a (int or float): Coefficient of x^2
        - b (int or float): Coefficient of x
        - c (int or float): Constant term
        """
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        """
        Return a string representation of the quadratic equation.
        """
        return f"{self.a}x^2 + {self.b}x + {self.c}"