# multiplication_table.py

This program takes a positive integer n and neatly prints an n x n multiplication table.

## Logic

1. Take an input n from the user (and check if it is a positive integer).
2. Loop through the range 1 to n+1, and print each row of the table.

## Code Explanation

> Take an input n from the user (and check if it is a positive integer).

```python
n = int(input("Enter n: "))

if n < 1:
    raise ValueError("n must be a positive integer.")
```

> Loop through the range 1 to n+1, and print each row of the table.

```python
for row in range(1,n+1):
    for col in range(1,n+1):
        print(f"{(row)*(col):3}", end=" ")
    print()
```

### Further explanation

`n` will be the maximum number of rows and columns in the table. Each row contains the multiples of the row number.

Example: `n = 10`

```python
1   2   3   4   5   6   7   8   9  10
2   4   6   8  10  12  14  16  18  20
3   6   9  12  15  18  21  24  27  30
...
```

For every column, print the product of the row number and the column number. For every row, print a newline after the last column.

```python
for row in range(1,n+1):
    for col in range(1,n+1):
        print(f"{(row)*(col):3}", end=" ")
    print()
```

In the f-string, `:3` means that the number will be padded with spaces to make it 3 characters long. This is to make the table look neat. Although this breaks at n > 31 since 32*32 = 1024, which is 4 characters long.

```python
print(f"{(row)*(col):3}", end=" ")
```

> Without `:3`

```powershell
PS > multiplication_table.py
Enter n: 8
1 2 3 4 5 6 7 8
2 4 6 8 10 12 14 16
3 6 9 12 15 18 21 24
4 8 12 16 20 24 28 32
5 10 15 20 25 30 35 40
6 12 18 24 30 36 42 48
7 14 21 28 35 42 49 56
8 16 24 32 40 48 56 64
```

> With `:3`

```powershell
PS > multiplication_table.py
Enter n: 8
  1   2   3   4   5   6   7   8
  2   4   6   8  10  12  14  16
  3   6   9  12  15  18  21  24
  4   8  12  16  20  24  28  32
  5  10  15  20  25  30  35  40
  6  12  18  24  30  36  42  48
  7  14  21  28  35  42  49  56
  8  16  24  32  40  48  56  64
```
