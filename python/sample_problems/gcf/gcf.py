"""
This program takes two positive integers A and B and finds their greatest common factor (GCF).
"""
# Tabamo, Euan Jed S.

# Define a function that computes the GCF of two numbers
def compute_GCF(num1, num2):
    gcf = 1

    # we can only check divisibility up to the smaller number
    smaller = num1 if num1 < num2 else num2

    for i in range(1, smaller + 1): # check divisibility from 1 to smaller
        if (num1 % i == 0 and num2 % i == 0): # if both are divisible by i, set gcf to i
            gcf = i
    return gcf # return the largest number that divides both num1 and num2

# Input
a = int(input("Enter A: "))
b = int(input("Enter B: "))

# Input validity
if a < 1 or b < 1:
    raise ValueError("A and/or B must be positive integers.")

# Call the function and print the result
gcf = compute_GCF(a,b)
print(f"The GCF is {gcf}.")