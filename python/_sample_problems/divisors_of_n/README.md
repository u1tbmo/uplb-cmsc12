# divisors_of_n.py

This program takes a positive integer n and prints all divisors of n.

## Logic

1. Take an input n.
2. Check if n is a valid input.
3. Loop through all numbers up to n and check if n is divisible by the numbers.
4. If n is divisible by a particular number, print the number.

## Code Explanation

> Get input and initialize variables

```python
n = int(input("Enter a number: "))

if n < 1:
    raise ValueError("Number must be a positive integer.")
```

> Loop through all numbers up to n and check if n is divisible by the numbers.

```python
for divisor in range(1, n+1):
    if n % divisor == 0:
        print(divisor)
```
