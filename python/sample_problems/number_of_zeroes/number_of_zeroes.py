"""
This program takes a positive integer n, followed by a list of n integers, and count the number of zeroes in the list.
"""
# Tabamo, Euan Jed S.
# Assuming that we are not to use lists.

count = 0

# Input
number_of_numbers = int(input("Numbers to input: "))

# Input validity
if number_of_numbers < 1:
    raise ValueError("Input must be at least one.")

for i in range(number_of_numbers):
    number = int(input("Enter a number: "))
    if number == 0:
        count += 1

print(f"Zero count: {count}")