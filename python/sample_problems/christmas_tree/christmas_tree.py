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
max_width_row = 3 + (2*(n-1)) # row with the maximum width
rows = 3 # number of rows of the current trapezoid

# Iterate through n trapezoids
while count < n:
    # Print the trapezoid
    for i in range(count, rows):
        spaces_bef_aft = max_width_row - i # number of spaces before and after the asterisks
        asterisks = 2*i + 1 # number of asterisks
        print("  "*spaces_bef_aft, end="")
        print("* "*asterisks, end="")
        print("  "*spaces_bef_aft)
    
    # Update the row and count for the next trapezoid
    rows += 2
    count += 1

# get the length of the max width row of the last trapezoid
max_length = len("  "*((2*max_width_row+1)))

# print a centered "Merry Christmas!" christmas_message
christmas_message = "Merry Christmas!"
christmas_message = christmas_message.center(max_length)
print(christmas_message)

