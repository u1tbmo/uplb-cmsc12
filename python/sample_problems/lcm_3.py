# Tabamo, Euan Jed S.
# Input three positive integers A, B, and C, and find the least common multiple of A, B, and C.

a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))

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

lcm = compute_LCM(a,b,c)
print(f"The LCM is {lcm}.")