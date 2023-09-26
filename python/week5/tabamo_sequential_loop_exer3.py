"""Draws a letter C based on input dimension"""
# Exercise 3a - Tabamo, Euan Jed S. - Sept 26, 2023

# Get input
dimension = int(input("Enter dimension: "))

# Iterate through each row in the 2D Dimension
for row in range(dimension):
    # if the row is the first or last row print "* " dimension times
    if (row == 0) or (row == dimension-1):
        print(("* " * dimension).strip())
    # if not, print "*"
    else:
        print("*")