# draw_boxes.py

This program takes two positive integers L and W and draws a box-shaped figure L chars long and W chars thick.

## Logic

1. Take inputs L and W.
2. Check if L and W are valid inputs.
3. Print the box row by row.

## Code Explanation

> Get input and initialize variables

```python
l = int(input("Enter L: "))
w = int(input("Enter W: "))

if l < 1 or w < 1:
    raise ValueError("Length and/or width must be positive integers.")
```

> Print the box row by row

```python
for row in range(l):
    for col in range(w):
        if row == 0 or row == l-1 or col == 0 or col == w-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

### Further explanation

The loop `for row in range(l)` iterates through the rows of the box. The loop `for col in range(w)` iterates through the columns of the box. The if statement checks if the current position is on the border of the box. If it is, it prints a star. Otherwise, it prints a space. The `print()` statement prints a newline character to move to the next row.

```powershell
PS > py draw_boxes.py
Enter L: 3
Enter W: 8
* * * * * * * *
*             *
* * * * * * * *
```

```powershell
PS > py draw_boxes.py
Enter L: 11
Enter W: 4
* * * *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
*     *
* * * *
```
