"""Draws a boxed X and X based on input dimension"""
# Exercise 3b - Tabamo, Euan Jed S. - Sept 26, 2023

# Get input
dimension = int(input("Enter dimension: "))

# Boxed X
# Iterate through each row and column in the 2D Dimension
rows = 0
while rows < dimension: # for every row
    cols = 0
    while cols < dimension: # for every column
        # print "*" if:
        # it is the first or last row,
        # or first or last column,
        # or the downward diagonal (cols == rows),
        # or the upward diagonal (cols + rows == dimension - 1)
        if (rows == dimension - 1) or (cols == dimension - 1) or (cols == 0) or (rows == 0) or (rows == cols) or (cols + rows == dimension - 1):
            print("*", end=" ")
        # otherwise print whitespace
        else:
            print(" ", end=" ")
        cols += 1
    print()
    rows += 1

print()

# X
rows = 0
while rows < dimension:
    cols = 0
    while cols < dimension:
        if (rows == cols) or (cols + rows == dimension - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        cols += 1
    print()
    rows += 1