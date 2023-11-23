"""This is a program that allows the user to find the factorial and to perform operations on factorials."""
# Factorial - Tabamo, Euan Jed S. - Oct 3, 2023

def factorial(x) -> int:
    """
    Returns the factorial given a number.

    Parameters:
        x (int): The input number to find the factorial of.

    Returns:
        result (int): The factorial of parameter x.
    """
    result = 1
    for i in range(x,0,-1):
        result *= i
    return result

RUNNING = True
while RUNNING:
    print()
    print("-------------------MENU-------------------")
    print("[1] Factorial of a number")
    print("[2] Sum of factorial of two numbers")
    print("[3] Difference of factorial of two numbers")
    print("[4] Exit the program")
    choice = int(input("\n[Choice] > "))
    match choice:
        case 1:
            n1 = int(input("Enter integer: "))
            print(factorial(n1))
        case 2:
            n1 = int(input("[1] Enter integer: "))
            n2 = int(input("[2] Enter integer: "))
            print(factorial(n1) + factorial(n2))
        case 3:
            n1 = int(input("[1] Enter integer: "))
            n2 = int(input("[2] Enter integer: "))
            print(factorial(n1) - factorial(n2))
        case 4:
            print("See you next time!")
            RUNNING = False
        case _:
            print("Unknown input!")