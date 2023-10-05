# gcf.py

This program takes two positive integers A and B and finds their greatest common factor (GCF).

## Logic

1. Define a function with two parameters, a and b that returns the GCF of a and b.
2. Take inputs a and b from the user (and check if they are positive integers).
3. Call the function with a and b as arguments and print the result.

## Code Explanation

> Define a function with two parameters, a and b that returns the GCF of a and b.

```python
def compute_GCF(num1, num2):
    gcf = 1

    smaller = num1 if num1 < num2 else num2

    for i in range(1, smaller + 1):
        if (num1 % i == 0 and num2 % i == 0):
            gcf = i
    return gcf
```

> Take inputs a and b from the user (and check if they are positive integers).

```python
a = int(input("Enter A: "))
b = int(input("Enter B: "))

if a < 1 or b < 1:
    raise ValueError("A and/or B must be positive integers.")
```

> Call the function with a and b as arguments and print the result.

```python
gcf = compute_GCF(a,b)
print(f"The GCF is {gcf}.")
```
