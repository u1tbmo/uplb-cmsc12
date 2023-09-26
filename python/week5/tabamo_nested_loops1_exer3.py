"""Draws a hollow right triangle based on input dimension"""
# Exercise 3b - Tabamo, Euan Jed S. - Sept 26, 2023

# Get input
dimension = int(input("Enter dimension: "))

rows = 0 # Initialize rows
while rows < dimension: # for every row in the 2D dimension
    cols = 0 # Initialize cols
    while cols < dimension: # for every column in the row
        # print "*" if:
        # it is currently the first column,
        # or the last row,
        # or the downward diagonal (rows == cols)
        if  (cols == 0) or (rows == dimension - 1) or (rows == cols):
            print("*", end=" ")

        # otherwise print whitespace
        else:
            print(" ", end=" ")

        cols += 1 # increment cols
    print() # for every row, print a new line
    rows += 1 # increment rows