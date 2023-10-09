"""
This program takes a positive integer n and draws a Christmas tree-shaped figure of chars, consisting of 'n' stacked centered trapezoids.
"""
# Tabamo, Euan Jed S.

# Input
n = int(input("Enter n: "))

# Input validity
if n < 1:
    raise ValueError("n must be positive")

# Initialize variables
count = 0 # number of trapezoids printed
half_width_bottom_row = 3 + (2*(n-1)) # calculates half of the width of the bottom row of the tree (since we will be using it twice per row)
rows = 3 # number of rows of the current trapezoid

# Iterate through n trapezoids
while count < n:
    # Print the trapezoid
    for i in range(count, rows):
        spaces_bef_aft = half_width_bottom_row - i # number of spaces before and after the asterisks
        asterisks = 2*i + 1 # number of asterisks
        print("  "*spaces_bef_aft, end="")
        print("* "*asterisks, end="")
        print("  "*spaces_bef_aft)
    
    # Update the row and count for the next trapezoid
    rows += 2
    count += 1

# get the length of the longest line
# since half_width_bottom_row is half of the width of the bottom row, we multiply it by 2 and add 1 to get the length of the longest line
max_length = len("  "*((2*half_width_bottom_row+1)))

# print a centered "Merry Christmas!" christmas_message
christmas_message = "Merry Christmas!"
christmas_message = christmas_message.center(max_length)
print(christmas_message)

