# Tabamo, Euan Jed S.
# Input a positive integer n, and determine whether n is prime (no divisors except 1 and itself)
# or composite (has divisors other than 1 and itself).

n = int(input("Enter a positive integer: "))

is_prime = True
for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break

match is_prime:
    case True:
        print(f"{n} is prime.")
    case False:
        print(f"{n} is composite.")