# Tabamo, Euan Jed S.
# Input a positive integer n and draw a Christmas tree-shaped figure of chars, consisting of n stacked “centered” trapezoids
n = int(input("Enter n: "))

if n < 1:
    raise ValueError("n must be positive")

# Logic
# n will not be the number of rows in the tree, but the number of trapezoids in the tree
# the pattern of the trapezoids is as follows:
# at trapezoid 1 => 1,3,5
# at trapezoid 2 => 3,5,7,9
# thus, the succeeding trapezoid starts with the length of previous trapezoid's second row
# the number of rows increase by 1 per trapezoid, but the number of starting stars increase by 2

count = 0 # keep track of the number of trapezoids printed
max_width_row = 3 + (2*(n-1)) # keep track of the number of largest row
rows = 3 # keep track of the number of rows in the current trapezoid

while count < n: # while there are still trapezoids to be printed
    for i in range(count,rows): # the range(count,rows) ensures that we start at the second row of the previous trapezoid
        print("  "*(max_width_row-i), end="") # print the spaces before the first star
        print("* "*(2*i+1), end="") # print the stars
        print("  "*(max_width_row-i)) # print the spaces after the last star
    rows += 2 # increase the number of rows by 2
    count += 1 # increase the number of trapezoids printed by 1

# get the length of the max width row of the last trapezoid
max_length = len("  "*((2*max_width_row+1)))

christmas_message = "Merry Christmas!"
christmas_message = christmas_message.center(max_length)

# print a centered "Merry Christmas!" christmas_message
print(christmas_message)

# How does this work?
# the normal function:
# for i in range(rows):
# would print rows starting from 1 regardless of the value of trapezoid currently being printed
# example:
# at trapezoid 1 => 1,3,5
# at trapezoid 2 => 1,3,5,7,9
# at trapezoid 3 => 1,3,5,7,9,11,13
# since we are counting the number of trapezoids printed, we can use that to determine the starting row
# using range(count,rows), we can omit the unnecessary rows
# example:
# at trapezoid 1 => 1,3,5
# at trapezoid 2 => 1,3,5,7,9 => range(1,5) => 3,5,7,9
# at trapezoid 3 => 1,3,5,7,9,11,13 => range(2,7) => 5,7,9,11,13
# the result is that it seems like each trapezoid is one row longer than the previous trapezoid