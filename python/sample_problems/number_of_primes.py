# Tabamo, Euan Jed S.
# Input an integer n and print the number of primes between n and 2n.

n = int(input("Enter a positive integer: "))

def prime(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

count = 0
for number in range(n,2*n):
    count += 1 if prime(number) else 0

print(f"There are {count} primes between {n} and {2*n}.")