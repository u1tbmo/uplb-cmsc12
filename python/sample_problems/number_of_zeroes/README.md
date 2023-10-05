# number_of_zeroes.py

This program takes a positive integer n, followed by a list of n integers, and count the number of zeroes in the list.

## Logic

1. Take an input n from the user (and check if it is a positive integer).
2. Take n more inputs from the user, for every input check if it is 0.
3. If it is 0, increment the counter by 1.
4. Print the counter.

### Code Explanation

> Take an input n from the user (and check if it is a positive integer).

```python
number_of_numbers = int(input("Numbers to input: "))

if number_of_numbers < 1:
    raise ValueError("Input must be at least one.")
```

> Take n more inputs from the user, for every input check if it is 0.
> If it is 0, increment the counter by 1.

```python
for i in range(number_of_numbers):
    number = int(input("Enter a number: "))
    if number == 0:
        count += 1
```

> Print the counter.

```python
print(f"Zero count: {count}")
```
