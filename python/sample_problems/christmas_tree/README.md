# christmas_tree.py

This program takes a positive integer n and draws a Christmas tree-shaped figure of chars, consisting of 'n' stacked centered trapezoids.

## Logic

1. Get an input from the user.
2. Check if the input is valid.
3. Print a trapezoid for each iteration up to n, with the trapezoid increasing its number of rows.

## Code Explanation

> Get input and initialize variables

```python
n = int(input("Enter n: "))

if n < 1:
    raise ValueError("n must be positive")

count = 0
max_width_row = 3 + (2*(n-1))
rows = 3
```

> Print the trapezoids

```python
while count < n:
    for i in range(count,rows):
        spaces_bef_aft = max_width_row - i
        asterisks = 2*i + 1
        print("  "*spaces_bef_aft, end="")
        print("* "*asterisks, end="")
        print("  "*spaces_bef_aft)
    rows += 2
    count += 1
```

> Print the Merry Christmas message.

```python
max_length = len("  "*((2*max_width_row+1)))

christmas_message = "Merry Christmas!"
christmas_message = christmas_message.center(max_length)
print(christmas_message)
```

### Further explanation

The initialized variables are as follows:

```python
count = 0
max_width_row = 3 + (2*(n-1))
rows = 3
```

The `count` variable is used to count the number of trapezoids printed.

The `max_width_row` variable is used to determine the maximum width of the trapezoid. This value comes from the following logic:
`n` is the number of trapezoids to be printed. The first trapezoid has a width of 3, and each trapezoid after that has a width that is 2 more than the previous trapezoid.

For example: If `n = 4`, there would be 4 trapezoids, with the following widths: `3,5,7,9`
Since we already know that the max width of the first trapezoid is always 3, we can add use `n-1` to get the number of trapezoids after the first one, and multiply that by 2 to get the number of additional asterisks for each trapezoid. Then we add the 3 back to get the total width.
Thus we get the formula: `3 + (2*(n-1))` for the maximum width of the christmas tree.

Regarding printing the trapezoids to create a christmas tree, the first intuition would be to use a loop like this:

```python
while count < n:
    for i in range(rows): # notice the missing start parameter
        spaces_bef_aft = max_width_row - i
        asterisks = 2*i + 1
        print("  "*spaces_bef_aft, end="")
        print("* "*asterisks, end="")
        print("  "*spaces_bef_aft)
    rows += 2
    count += 1
```

In this code, we print each trapezoid (triangle actually since there is a semantic error in this code) by printing rows of asterisks. The number of asterisks in each row is determined by the formula `2*i + 1`, where `i` is the current row number. The number of spaces before and after the asterisks is determined by the formula `max_width_row - i`, where `i` is the current row number.

This means that since we already know the maximum width of the trapezoid, we can use that to determine the number of spaces before and after the asterisks, we just decrease the spaces by 2 for each row since we are increasing the number of asterisks by 2 for each row. Remember that `spaces_bef_aft` is the number of spaces before and after the asterisks, so we multiply that by 2 to get the total number of spaces.

The problem with this code is that it would print rows starting from 1 regardless of which trapezoid is currently being printed.

Meaning to say, for example:

- `n = 0 => 1,3,5`
- `n = 1 => 1,3,5,7,9`
- `n = 2 => 1,3,5,7,9,11,13`

```powershell
PS > py christmas_tree.py
Enter n: 3
              *
            * * *
          * * * * *
              *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
              *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
    * * * * * * * * * * *
  * * * * * * * * * * * * *
       Merry Christmas!
```

Since we are counting the number of trapezoids printed, we can use that to determine the starting row.

Using `range(count,rows)`, we can omit the unnecessary rows

example:

- `n = 0 => 1,3,5 => range(0,3) => 1,2,3`
- `n = 1 => 1,3,5,7,9 => range(1,5) => 3,5,7,9`
- `n = 2 => 1,3,5,7,9,11,13 => range(2,7) => 5,7,9,11,13`

```powershell
PS > py christmas_tree.py
Enter n: 3
              *
            * * *
          * * * * *
            * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
    * * * * * * * * * * *
  * * * * * * * * * * * * *
       Merry Christmas!
```

The result is that it seems like each trapezoid is one row longer than the previous trapezoid.
