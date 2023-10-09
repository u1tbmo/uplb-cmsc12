"""
This program takes a positive integer n and draws an isosceles triangle-shaped figure of chars, of height n.
"""
# Tabamo, Euan Jed S.

# Input
n = int(input("Enter n: "))

# Input validity
if n < 1:
    raise ValueError("n must be a positive integer.")

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
        print(" "*(n-i))
        continue

    print(" "*(n-i), end="")
    print("*", end="")
    print(" "*(2*i-1), end="")
    print("*", end="")
    print(" "*(n-i))