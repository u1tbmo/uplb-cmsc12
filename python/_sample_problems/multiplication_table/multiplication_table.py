"""
This program takes a positive integer n and neatly prints an n x n multiplication table.
"""
# Tabamo, Euan Jed S.

# Input
n = int(input("Enter n: "))

# Input validity
if n < 1:
    raise ValueError("n must be a positive integer.")

for row in range(1,n+1):
    for col in range(1,n+1):
        # :3 ensures that the string is 3 characters long at minimum (thus the table breaks for n > 31, since 32*32 = 1024)
        print(f"{(row)*(col):3}", end=" ") # end removes the newline
    print()
