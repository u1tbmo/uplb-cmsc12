# lcm.py

This program takes two positive integers A and B, and finds the least common multiple of A and B.

## Logic

1. Define a function `lcm(a,b)` that takes two positive integers `a` and `b` and returns their least common multiple.
2. Take two inputs `a` and `b` from the user (and check if they are positive integers).
3. Print the least common multiple of `a` and `b`.

## Code Explanation

> Define a function `lcm(a,b)` that takes two positive integers `a` and `b` and returns their least common multiple.

```python
def compute_LCM(num1, num2):
    lcm = None

    greater = num1 if num1 > num2 else num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm
```

> Take two inputs `a` and `b` from the user (and check if they are positive integers).

```python
a = int(input("Enter A:"))
b = int(input("Enter B:"))

if a < 1 or b < 1:
    raise ValueError("A and B must be positive integers.")
```

> Print the least common multiple of `a` and `b`.

```python
lcm = compute_LCM(a,b)
print(f"The LCM is {lcm}.")
```

### Further explanation

The least common multiple of two numbers is the smallest number that is a multiple of both of them.
The LCM is always larger than or equal to the larger of the two numbers.
That means if we encounter a number greater than or equal to the larger of the two numbers that is divisible by both of them, we can stop searching and return that number.

```python
def compute_LCM(num1, num2):
    lcm = None

    greater = num1 if num1 > num2 else num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm
```

## lcm3.py

This program takes three positive integers A, B, and C, and finds the least common multiple of A, B, and C.

### Logic for lcm3.py

The logic is exactly the same as the logic for finding the least common multiple of two numbers, the function just takes three numbers instead of two and also checks if the number is divisible by the third number.

```python
def compute_LCM(num1, num2, num3):
    lcm = None

    greatest = max(a,b,c)

    while True:
        if greatest % num1 == 0 and greatest % num2 == 0 and greatest % num3 == 0:
            lcm = greatest
            break
        greatest += 1

    return lcm
```
