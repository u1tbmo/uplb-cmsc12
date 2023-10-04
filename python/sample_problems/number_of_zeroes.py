# Tabamo, Euan Jed S.
# Assuming that we are not to use lists.
# Input an integer n, followed by a list of n integers, and count the number of zeroes in the list.

count = 0

number_of_numbers = int(input("Numbers to input: "))

for i in range(number_of_numbers):
    number = int(input("Enter a number: "))
    if number == 0:
        count += 1

print(f"Zero count: {count}")