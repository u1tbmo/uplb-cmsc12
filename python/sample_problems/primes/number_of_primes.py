"""
This program takes a positive integer n and prints the number of primes between n and 2n.
"""
# Tabamo, Euan Jed S.

# Input
n = int(input("Enter a positive integer: "))

# Input validation
if n < 2:
    raise ValueError("Input must be at least two.")

def prime(n):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

count = 0
for number in range(n,2*n):
    count += 1 if prime(number) else 0

print(f"There are {count} primes between {n} and {2*n}.")