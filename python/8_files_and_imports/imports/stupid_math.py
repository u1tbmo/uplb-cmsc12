"""
A module containing random functions that are definitely not useful.
"""

def add(a, b):
    """
    Adds two numbers together.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divides two numbers.
    """
    return a / b

def lim_divide_by_zero_from_right(a):
    """
    Divides by zero where zero is an arbitrarily small positive number.
    Not really, but it's close enough.
    """
    if a > 0:
        return f"The limit of {a}/x as x approaches 0+ is ∞"
    elif a < 0:
        return f"The limit of {a}/x as x approaches 0+ is -∞"
    else:
        return f"The limit of {a}/x as x approaches 0+ is undefined"
    
def lim_divide_by_zero_from_left(a):
    """
    Divides by zero where zero is an arbitrarily small negative number.
    Not really, but it's close enough.
    """
    if a > 0:
        return f"The limit of {a}/x as x approaches 0- is -∞"
    elif a < 0:
        return f"The limit of {a}/x as x approaches 0- is ∞"
    else:
        return f"The limit of {a}/x as x approaches 0- is undefined"