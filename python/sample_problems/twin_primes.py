# Tabamo, Euan Jed S.
# Twin primes are prime numbers that differ by two, (e.g. 3 and 5 is the smallest pair of twin
# primes). Find and print the first thirty (30) pairs of twin primes.

# Initialize twin prime count to 0.
count = 0

def prime(n):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

def twin_prime(num1, num2):
    difference = num1 - num2
    if difference < 0:
        difference *= -1
    is_twin_prime = True if difference == 2 else False
    return is_twin_prime

# We start from 3 because we already know that 2 is the only even prime number.
# From here, we can just add 2 to the previous number to get the next odd number.
i = 3
while count < 30:
    if prime(i) and twin_prime(i,i+2):
        count += 1
        print(f"{count}: ({i},{i+2})")
    i += 1