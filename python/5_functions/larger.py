"""Prints the largest number among two inputted numbers."""


def larger(num1, num2):
    """
    Prints the largest number among two inputted numbers.
    Parameters:
        num1 (int): the first number to be compared
        num2 (int): the second number to be compared
    Returns:
        Returns the larger number
    """
    return num1 if num1 > num2 else num2

x = int(input("[1] Enter a number:"))
y = int(input("[2] Enter a number:"))

print(larger(x,y))
