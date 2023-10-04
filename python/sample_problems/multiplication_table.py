# Tabamo, Euan Jed S.
# Input a positive integer n and neatly print an n x n multiplication table.

n = int(input("Enter n: "))

# n will be the maximum number of rows and columns in the table.
# each row contains the multiples of the row number
# example: n = 10
# 1   2   3   4   5   6   7   8   9  10
# 2   4   6   8  10  12  14  16  18  20
# 3   6   9  12  15  18  21  24  27  30 etc...

for row in range(n):
    for col in range(n):
        # row+1 and col+1 because we want to start at 1
        # :3 ensures that the string is 3 characters long at minimum (thus the table breaks for n > 31, since 32*32 = 1024)
        print(f"{(row+1)*(col+1):3}", end=" ") # end removes the newline
    print()
