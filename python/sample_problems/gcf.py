# Tabamo, Euan Jed S.
# Input two positive integers A and B.
# Find the GCF of A and B.

a = int(input("Enter A:"))
b = int(input("Enter B:"))

def compute_GCF(num1, num2):
    gcf = 1

    # choose the smaller number
    smaller = num1 if num1 < num2 else num2

    for i in range(1, smaller + 1): # check divisibility from 1 to smaller
      if (num1 % i == 0 and num2 % i == 0):
         gcf = i
    return gcf

gcf = compute_GCF(a,b)
print(f"The GCF is {gcf}.")