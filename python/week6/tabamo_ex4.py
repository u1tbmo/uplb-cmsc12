"""A program that will unlock the secret message using a security PIN."""
# Exercise 4 - Tabamo, Euan Jed S. - Oct 3, 2023

security_pin = None
MESSAGE = "Slay beshiee!!! Tama at korek na korek ang iyong inilagay na personal identification number!!!!!!"

def menu() -> int:
    """Prints a menu and asks for a choice.

    Returns:
        int: the choice of the user
    """
    # Print the menu
    print(
        "\n",
        "============= MENU =============\n",
        "|   [0] Exit Program           |\n",
        "|   [1] Unlock Secret Message  |\n",
        "|   [2] Change Security PIN    |\n",
        "================================"
    )

    # Ask for a choice
    num = int(input("[Choice] > "))
    return num

def secret_message(securityPin) -> str:
    """Prints the secret message if the PIN is correct.

    Args:
        securityPin (str): the current security PIN

    Returns:
        str: the security PIN
    """
    # If there is no PIN, manage the PIN.
    if securityPin is None:
        securityPin = manage_pin(securityPin)
        return securityPin

    # If there is a PIN
    # If the PIN is correct, print the secret message.
    input_pin = input("Enter your PIN: ")
    if input_pin == securityPin:
        print(
            "========THE SECRET MESSAGE========\n",
            MESSAGE
            )
        return securityPin
    # If the PIN is incorrect, return the PIN, do not print the message.
    else:
        print("Incorrect PIN!")
        return securityPin
    
    # This function always returns the securityPin.
    return securityPin

def manage_pin(securityPin) -> str:
    """Allows the user to manage the security PIN.

    Args:
        securityPin (str): the current security PIN

    Returns:
        str: the security PIN
    """
    # If there is no PIN, ask for a PIN.
    if securityPin is None:
        print("No Security PIN!")
        while securityPin is None:
            new_pin = input("Please enter a new PIN (length of 4): ")
            if not new_pin.isalnum() or not len(new_pin) == 4:
                print("Invalid PIN.")
            else:
                securityPin = new_pin
                print("Security PIN Enabled!")
                return securityPin

    # If there is a PIN, ask for the PIN
    # If the PIN is correct, ask the user to change the PIN.
    input_pin = input("Enter your PIN: ")
    if input_pin == securityPin:
        managing_pin = True
        while managing_pin:
            new_pin = input("Please change your PIN (length of 4): ")
            if not new_pin.isalnum() or not len(new_pin) == 4:
                print("Invalid PIN.")
            else:
                securityPin = new_pin
                print("Security PIN has been changed!")
                return securityPin
    # If the PIN is incorrect, return the securityPin which has not been changed.
    else:
        print("Wrong PIN!")
        return securityPin

    # This function always returns the securityPin.
    return securityPin

# MAIN PROGRAM LOOP
RUNNING = True
while RUNNING:
    choice = menu()
    if choice == 0:
        RUNNING = False
        print("See you next time!")
    elif choice == 1:
        security_pin = secret_message(security_pin)
    elif choice == 2:
        security_pin = manage_pin(security_pin)
    else:
        print("Invalid choice: Please select a valid option.")
