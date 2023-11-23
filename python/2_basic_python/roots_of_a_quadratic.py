"""This program computes the roots of a quadratic equation."""
# Assessment - Submitted by Tabamo, Euan Jed S.

import math

# Get the values of a, b, and c from the user.
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
c = input("Enter the value of c: ")

# Convert the values to float
a = float(a)
b = float(b)
c = float(c)

# Compute the discriminant
# if discriminant is negative, there are no real roots
# if discriminant is zero, there is one real root
# if discriminant is positive, there are two real roots
discriminant = b**2 - 4*a*c

# Compute for the roots
if discriminant < 0:
    print("There are no real roots.")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"There is one real root: {root}")
else:
    root1 = -b + math.sqrt(discriminant) / (2*a)
    root2 = -b - math.sqrt(discriminant) / (2*a)
    print(f"There are two real roots: {root1} and {root2}")