# Tabamo, Euan Jed S.
# Input two positive integers A and B, and find the least common multiple of A and B, i.e., the
# smallest integer that is both a multiple of A and B.

a = int(input("Enter A:"))
b = int(input("Enter B:"))

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

lcm = compute_LCM(a,b)
print(f"The LCM is {lcm}.")