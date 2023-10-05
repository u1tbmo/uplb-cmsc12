"""
This program takes two positive integers L and W and draws a box-shaped figure L chars long and W chars thick.
"""
# Tabamo, Euan Jed S.

# Input
l = int(input("Enter L: "))
w = int(input("Enter W: "))

# Input validity
if l < 1 or w < 1:
    raise ValueError("Length and/or width must be positive integers.")

# Draw box-shaped figure
for row in range(l):
    for col in range(w):
        if row == 0 or row == l-1 or col == 0 or col == w-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()