"""
This program takes two positive integers A and B, and finds the least common multiple of A and B.
"""
# Tabamo, Euan Jed S.

# Define a function that takes two positive integers and returns their LCM
def compute_LCM(num1, num2):
    lcm = None

    # the LCM is always greater than or equal to the greater number
    greater = num1 if num1 > num2 else num2

    # check numbers greater than or equal to the greater number for a number that is divisible by both num1 and num2
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1

    return lcm

# Input
a = int(input("Enter A:"))
b = int(input("Enter B:"))

# Input validity
if a < 1 or b < 1:
    raise ValueError("A and B must be positive integers.")

# Call the function and print the result
lcm = compute_LCM(a,b)
print(f"The LCM is {lcm}.")