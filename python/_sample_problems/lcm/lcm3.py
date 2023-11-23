"""This program takes three positive integers A, B, and C, and finds the least common multiple of A, B, and C."""
# Tabamo, Euan Jed S.

# Define a function that takes three positive integers and returns their LCM
def compute_LCM(num1, num2, num3):
    lcm = None

    # the LCM is always greatest than or equal to the largest number
    greatest = max(a,b,c)

    # check numbers greatest than or equal to the greatest number for a number that is divisible by num1,num2, and num3
    while True:
        if greatest % num1 == 0 and greatest % num2 == 0 and greatest % num3 == 0:
            lcm = greatest
            break
        greatest += 1

    return lcm

# Input
a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))

# Input validity
if a < 1 or b < 1 or c < 1:
    raise ValueError("A, B, and C must be positive integers.")

# Call the function and print the result
lcm = compute_LCM(a,b,c)
print(f"The LCM is {lcm}.")