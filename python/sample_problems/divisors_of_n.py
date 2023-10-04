# Input an integer n and print all divisors of n.
# Example: n = 12, divisors = 1, 2, 3, 4, 6, 12

n = int(input("Enter a number: "))

for divisor in range(1, n+1):
    if n % divisor == 0:
        print(divisor)