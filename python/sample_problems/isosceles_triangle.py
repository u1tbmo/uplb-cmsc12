# Tabamo, Euan Jed S.
# Input a positive integer n and draw an isosceles triangle-shaped figure of chars, of height n.

n = int(input("Enter n: "))

# LOGIC
# n will be the number of rows in the triangle
# n will also be the number of stars in the base of the triangle
# as we iterate through the rows, we will print n-i spaces, then 2i-1 chars, then n-i spaces again
# n-i refers to the space before the first char and after the last char
# 2i-1 refers to the space between the first char and the last char

for i in range(n):
    # 1st row is a special case
    if i == 0:
        print(" "*(n-i), end="")
        print("*", end="")
        print(" "*(n-i))
        continue
    # if it is the last row, print n chars
    if i == n-1: # n-1 because we start at 0
        print(" "*(n-i), end="")
        print("* "*n, end="")
        print(" "*(n-i), end="")
        continue

    print(" "*(n-i), end="")
    print("*", end="")
    print(" "*(2*i-1), end="")
    print("*", end="")
    print(" "*(n-i))