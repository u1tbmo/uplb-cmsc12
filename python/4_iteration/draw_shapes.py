"""Creates shapes based on input"""
# Tabamo, Euan Jed S. - Sep 26

# Get input
dimension = int(input("Enter dimension: "))

# Hollowed Square

row = 0
while row < dimension:
    col = 0
    while col < dimension:
        if ((row == 0) or (row == (dimension - 1)) or (col == 0) or (col == (dimension - 1))):
            print("* ", end="")
        else:
            print("  ", end="")
        col += 1
    print() # prints a new line
    row += 1

print()

# Filled Right Triangle

col = 1
for row in range(dimension):
    print("* " * col)
    col += 1

print()

# Filled Right Triangle Upside Down

row = 0
while row < dimension:
    col = 0
    while col < dimension:
        if row <= col:
            print("* ", end = "")
        else:
            print("  ", end="")
        col += 1
    print()
    row += 1

