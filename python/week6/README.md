# tabamo_ex4.py

A program that will unlock the secret message using a security PIN.

## Logic

1. Initialize a pin and a message.
2. Create three functions, one that prints the menu, one that prints the message when the pin is correct, and one that allows the user to manage the pin.

### Menu Function

This function prints the menu and asks for a choice.
It returns the choice of the user.

```python
def menu() -> int:
    print(
        "\n",
        "============= MENU =============\n",
        "|   [0] Exit Program           |\n",
        "|   [1] Unlock Secret Message  |\n",
        "|   [2] Change Security PIN    |\n",
        "================================"
    )

    num = int(input("[Choice] > "))
    return num
```

### Secret Message Function

This function prints the secret message if the pin is correct.

```python
def secret_message(securityPin) -> str:
    if securityPin is None:
        securityPin = manage_pin(securityPin)
        return securityPin

    input_pin = input("Enter your PIN: ")
    if input_pin == securityPin:
        print(
            "========THE SECRET MESSAGE========\n",
            MESSAGE
            )
        return securityPin
    else:
        print("Incorrect PIN!")
        return securityPin
    
    return securityPin
```

### Manage Pin Function

This function allows the user to manage the security PIN.

```python
def manage_pin(securityPin) -> str:
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
    else:
        print("Wrong PIN!")
        return securityPin

    return securityPin
```

## Main Program Loop

This is the main program loop.

```python
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
```

## Explanation

Once the program starts, the variables `security_pin` and `MESSAGE` are initialized.

```python
security_pin = None
MESSAGE = "Slay beshiee!!! Tama at korek na korek ang iyong inilagay na personal identification number!!!!!!"
```

Then, `RUNNING` is initialized and the loop will run. With this the menu will be printed.

```python
RUNNING = True
while RUNNING:
    choice = menu()
```

This calls the `menu()` function and stores the return value to the variable `choice`.

```python
def menu() -> int:
    print(
        "\n",
        "============= MENU =============\n",
        "|   [0] Exit Program           |\n",
        "|   [1] Unlock Secret Message  |\n",
        "|   [2] Change Security PIN    |\n",
        "================================"
    )

    num = int(input("[Choice] > "))
    return num
```

This displays the following.

```console
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] >
```

Once the user inputs a choice, the program will check if the choice is valid.

```python
    if choice == 0:
        RUNNING = False
        print("See you next time!")
    elif choice == 1:
        security_pin = secret_message(security_pin)
    elif choice == 2:
        security_pin = manage_pin(security_pin)
    else:
        print("Invalid choice: Please select a valid option.")
```

## Scenario 1: Exit Program

If the user inputs `0`, the program will exit since the `RUNNING` variable is set to `False` and the loop can no longer run.

```python
    if choice == 0:
        RUNNING = False
        print("See you next time!")
```

## Scenario 2: Unlock Secret Message, No Security PIN

If the user inputs `1`, the program will call the `secret_message()` function, with parameter `security_pin` which is `None` by default, then store the return value to the variable `security_pin`.

```python
    elif choice == 1:
        security_pin = secret_message(security_pin)
```

The secret message function will then run.

```python
def secret_message(securityPin) -> str:
    if securityPin is None:
        securityPin = manage_pin(securityPin)
        return securityPin

    input_pin = input("Enter your PIN: ")
    if input_pin == securityPin:
        print(
            "========THE SECRET MESSAGE========\n",
            MESSAGE
            )
        return securityPin
    else:
        print("Incorrect PIN!")
        return securityPin
    
    return securityPin
```

Since `security_pin` is `None`, the program will call the `manage_pin()` function, with parameter `securityPin`, then store the return value to the variable `securityPin`.

```python
    if securityPin is None:
        securityPin = manage_pin(securityPin)
        return securityPin
```

## Scenario 3: Manage Security PIN, No Security PIN

This scenario triggers when the user inputs `2` and the `security_pin` is `None`.

```python
    elif choice == 2:
        security_pin = manage_pin(security_pin)
```

It also triggers when the user inputs `1` and the `securityPin` is `None` since the `secret_message()` function calls the `manage_pin()` function.

```python
    if securityPin is None:
        securityPin = manage_pin(securityPin)
        return securityPin
```

The `manage_pin()` function will then run.

```python
def manage_pin(securityPin) -> str:
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
    else:
        print("Wrong PIN!")
        return securityPin

    return securityPin
```

Since `securityPin` is `None`, the following code will run.

```python
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
```

This code will continually run until the user inputs a valid security PIN. The security_pin is validated using the `isalnum()` and `len()` functions.

```python
            if not new_pin.isalnum() or not len(new_pin) == 4:
                print("Invalid PIN.")
```

Sample Output:

```console
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 2
No Security PIN!
Please enter a new PIN (length of 4): ab^2     
Invalid PIN.
Please enter a new PIN (length of 4): 000000
Invalid PIN.
Please enter a new PIN (length of 4): 36712
Invalid PIN.
Please enter a new PIN (length of 4): ab12
Security PIN Enabled!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 
```

Note though that if this scenario is triggered by the `secret_message()` function, the `security_pin` will be returned to the `secret_message()` function, not the main program loop. Though, the security PIN will then be returned to the main program loop by the `secret_message()` function.

```python
    if securityPin is None:
        securityPin = manage_pin(securityPin)
        return securityPin
```

The returned value will then be assigned to the variable `security_pin` in the main program loop. Which means that the security PIN will be saved.

```python
    elif choice == 1:
        security_pin = secret_message(security_pin)
    elif choice == 2:
        security_pin = manage_pin(security_pin)
```

## Scenario 4: Unlock Secret Message, With Security PIN

If the user inputs `1`, the program will call the `secret_message()` function, with parameter `security_pin` which is not `None`, then store the return value to the variable `security_pin`.

```python
    elif choice == 1:
        security_pin = secret_message(security_pin)
```

The secret message function will then run. Since `securityPin` is not `None`, the following code will run.

```python
    input_pin = input("Enter your PIN: ")
    if input_pin == securityPin:
        print(
            "========THE SECRET MESSAGE========\n",
            MESSAGE
            )
        return securityPin
    else:
        print("Incorrect PIN!")
        return securityPin
    
    return securityPin
```

The user will be asked to input a security PIN. If the user inputs the correct security PIN, the secret message will be printed.

```python
    if input_pin == securityPin:
        print(
            "========THE SECRET MESSAGE========\n",
            MESSAGE
            )
        return securityPin
```

Sample Output:

```console
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
Enter your PIN: ab12
========THE SECRET MESSAGE========
 Slay beshiee!!! Tama at korek na korek ang iyong inilagay na personal identification number!!!!!!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] >
```

Otherwise, the function prints an error message and prematurely ends the function. Since the securityPin did not change, the security PIN will be returned to the main program loop and assigned to the variable `security_pin` again, which does nothing.

```python
    else:
        print("Incorrect PIN!")
        return securityPin
```

Sample Output:

```console
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
Enter your PIN: notv
Incorrect PIN!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] >
```

## Scenario 5: Manage Security PIN, With Security PIN

This scenario triggers when the user inputs `2` and the `security_pin` is not `None`.

```python
    elif choice == 2:
        security_pin = manage_pin(security_pin)
```

The `manage_pin()` function will then run. Since `securityPin` is not `None`, the following code will run.

```python
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
    else:
        print("Wrong PIN!")
        return securityPin

    return securityPin
```

If the entered security PIN is correct, the user will be asked to input a new security PIN. The security PIN is then validated again using the `isalnum()` and `len()` functions and the user will be continually asked to input a new security PIN until a valid one is entered.

```python
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
```

Sample Output:

```console
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 2
Enter your PIN: ab12
Please change your PIN (length of 4): abcd
Security PIN has been changed!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] >
```

Otherwise, the function prematurely ends and returns the security PIN to the main program loop (which again does nothing since the security PIN was not changed).

```python
    else:
        print("Wrong PIN!")
        return securityPin
```

Sample Output:

```console
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 2
Enter your PIN: zx89
Wrong PIN!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] >
```

## Sample Output

```console
PS > py tabamo_ex4.py
 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
No Security PIN!
Please enter a new PIN (length of 4): ab12
Security PIN Enabled!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
Enter your PIN: mcdo
Incorrect PIN!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
Enter your PIN: ab12
========THE SECRET MESSAGE========
 Slay beshiee!!! Tama at korek na korek ang iyong inilagay na personal identification number!!!!!!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 2
Enter your PIN: mcdo 
Wrong PIN!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 2
Enter your PIN: ab12
Please change your PIN (length of 4): jbee
Security PIN has been changed!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
Enter your PIN: mcdo
Incorrect PIN!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 1
Enter your PIN: jbee
========THE SECRET MESSAGE========
 Slay beshiee!!! Tama at korek na korek ang iyong inilagay na personal identification number!!!!!!

 ============= MENU =============
 |   [0] Exit Program           |
 |   [1] Unlock Secret Message  |
 |   [2] Change Security PIN    |
 ================================
[Choice] > 0
See you next time!
```
