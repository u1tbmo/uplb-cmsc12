# Tabamo, Euan Jed S.
# Input positive integers L and W and draw a box-shaped figure L chars long and W chars thick.

l = int(input("Enter L: "))
w = int(input("Enter W: "))

for row in range(l):
    for col in range(w):
        if row == 0 or row == l-1:
            print("*", end=" ")
        else:
            if col == 0 or col == w-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()