"""
This program takes a positive integer n, and determines whether n is prime or composite.
"""
# Tabamo, Euan Jed S.

# Input
n = int(input("Enter a positive integer: "))

# Input validity
if n < 2:
    raise ValueError("n must be at least two.")

is_prime = True
for i in range(2,int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break

match is_prime:
    case True:
        print(f"{n} is prime.")
    case False:
        print(f"{n} is composite.")