def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def divide(a, b):
    """Returns the quotient of two numbers."""
    if b == 0:
        return 'Error: Cannot divide by zero'
    return a / b
