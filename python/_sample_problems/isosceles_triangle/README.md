# isosceles_triangle.py

This program takes a positive integer n and draws an isosceles triangle-shaped figure of chars, of height n.

## Logic

1. Take an input n from the user (and check if it is a positive integer).
2. Loop through the range 1 to n+1, and print each row of the triangle.

## Code Explanation

> Take an input n from the user (and check if it is a positive integer).

```python
n = int(input("Enter n: "))

if n < 1:
    raise ValueError("n must be a positive integer.")
```

> Loop through the range 1 to n+1, and print each row of the triangle.

```python
for i in range(n):
    if i == 0:
        print(" "*(n-i), end="")
        print("*", end="")
        print(" "*(n-i))
        continue

    if i == n-1:
        print(" "*(n-i), end="")
        print("* "*n, end="")
        print(" "*(n-i), end="")
        continue

    print(" "*(n-i), end="")
    print("*", end="")
    print(" "*(2*i-1), end="")
    print("*", end="")
    print(" "*(n-i))
```

### Further explanation

`n` will be the number of rows in the triangle

If it is the first row, we will print `n-i` spaces, then a single star, then `n-i` spaces again.

```python
if i == 0:
    print(" "*(n-i), end="")
    print("*", end="")
    print(" "*(n-i))
    continue
```

If it is the last row, we will print `n-i` spaces, then `n` stars, then `n-i` spaces again.  `n` will be the number of stars in the base of the triangle

```python
if i == n-1:
    print(" "*(n-i), end="")
    print("* "*n, end="")
    print(" "*(n-i), end="")
    continue
```

If it is currently the row between the first and last row, we will print `n-i` spaces, then `2i-1` chars, then `n-i` spaces again

- `n-i` refers to the space before the first char and after the last char
- `2i-1` refers to the space between the first char and the last char

```python
print(" "*(n-i), end="")
print("*", end="")
print(" "*(2*i-1), end="")
print("*", end="")
print(" "*(n-i))
```
