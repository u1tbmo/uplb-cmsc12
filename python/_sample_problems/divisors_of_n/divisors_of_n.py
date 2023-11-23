"""
This program takes a positive integer n and prints all divisors of n.
"""
# Tabamo, Euan Jed S.

# Input
n = int(input("Enter a number: "))

# Input validity
if n < 1:
    raise ValueError("Number must be a positive integer.")

# Print all divisors of n
for divisor in range(1, n+1):
    if n % divisor == 0:
        print(divisor)