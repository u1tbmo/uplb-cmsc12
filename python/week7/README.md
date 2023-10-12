# tabamo_ex5.py

This program encrypts a list of text using Caesar’s Cipher in two levels.

## Logic

1. Initialize the needed variables.
2. Define the needed functions.
3. Make a main program loop that prints the menu and asks for the user’s choice.
4. Make decision statements for the user’s choice.
5. Proceed to each function depending on the user’s choice.

## Functions

### Main Program Loop

```python
# Main Program Loop
RUNNING = True
while RUNNING:
    choice = menu()
    if choice == 1:
        text_list, encrypted_1, encrypted_2 = enter_text(text_list, encrypted_1, encrypted_2)

    elif choice == 2:
        encrypted_1, encrypted_2 = encrypt(text_list, encrypted_1, encrypted_2)

    elif choice == 3:
        view_encrypted(text_list, encrypted_1, encrypted_2)

    elif choice == 4:
        RUNNING = False
        print("Bye!")

    else:
        print("Invalid choice!")
```

### `encrypt_text(text, key)`

```python
def encrypt_text(text, key) -> str:
    """This function encrypts text using a key.

    This version uses the maketrans() and translate() methods for strings.

    Arguments:
        text (str) - the text to be encrypted
        key (int) - the rotational key for the cypher

    Returns:
        str - the encrypted text
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = alphabet[key:] + alphabet[:key]

    mapping_table = str.maketrans(alphabet + alphabet.upper(), cipher + cipher.upper())

    return text.translate(mapping_table)
```

### `encrypt_text_loop_version(text, key)`

```python
def encrypt_text_loop_version(text, key) -> str:
    """This function encrypts text using a key.

    This version uses a for loop to iterate through every character in the text.

    Arguments:
        text (str) - the text to be encrypted
        key (int) - the rotational key for the cypher

    Returns:
        str - the encrypted text
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = alphabet[key:] + alphabet[:key]

    encrypted_text = ''

    for c in text:
        if c.isalpha():
            index = alphabet.index(c.lower())
            if c.isupper():
                encrypted_text += cipher[index].upper()
            else:
                encrypted_text += cipher[index]
        else:
            encrypted_text += c
    return encrypted_text
```

### `menu()`

```python
def menu() -> int:
    """This function prints a menu and asks the user for a choice.

    Returns:
        int - the choice
    """

    print(
        "\n"
        "==========================\n",
        "[1] Enter Lists of Text/s \n",
        "[2] Encrypt               \n",
        "[3] View Encrypted        \n",
        "[4] Exit                  ",
    )

    return int(input("Enter Choice: "))
```

### `enter_text(t_lst, enc1, enc2)`

```python
def enter_text(t_lst, enc1, enc2) -> list:
    """This function allows the user to create a list of text and add it to the list.

    Args:
        t_lst (list): the list of text
        enc1 (list): the list of first level encrypted text
        enc2 (list): the list of second level encrypted text

    Returns:
        list: the list of the three lists
    """

    t_lst.clear()
    enc1.clear()
    enc2.clear()

    num_of_inputs = int(input("Number of text inputs: "))

    for i in range(num_of_inputs):
        element = input(f"[{i + 1}] ")
        t_lst.append(element)

    return [t_lst, enc1, enc2]
```

### `encrypt(t_lst, enc1, enc2)`

```python
def encrypt(t_lst, enc1, enc2) -> list:
    """This function encrypts the text in the list of text in two levels.

    Args:
        t_lst (list): the list of text
        enc1 (list): the list of first level encrypted text
        enc2 (list): the list of second level encrypted text

    Returns:
        list: the list of both encrypted text lists
    """

    if len(t_lst) == 0:
        print("Enter list of text first.")
        return [enc1, enc2]

    enc1.clear()
    enc2.clear()

    key1 = int(input("First Level Shift: "))
    key2 = int(input("Second Level Shift: "))

    if key1 > 26 or key1 < -26:
        key1 = key1 % 26
    if key2 > 26 or key2 < -26:
        key2 = key2 % 26

    for text in t_lst:
        enc_text_1 = encrypt_text(text, key1)
        enc1.append(enc_text_1)

    for text in enc1:
        enc_text_2 = encrypt_text(text, key2)
        enc2.append(enc_text_2)

    return [enc1, enc2]
```

### `view_encrypted(t_lst, enc1, enc2)`

```python
def view_encrypted(t_lst, enc1, enc2) -> None:
    """This function allows the user to see the encryption process.
    """

    if len(enc1) == 0 or len(enc2) == 0:
        print("No ciphered text yet!")

    else:
        for i in range(len(t_lst)):
            print(f"[{i+1}] {t_lst[i]} ===> {enc1[i]} ===> {enc2[i]}")
```

## Further explanation

### `encrypt_text()`, explained

This function uses the `maketrans()` and `translate()` methods for strings.  
The `maketrans()` method creates a mapping table for translation.  
The `translate()` method uses the mapping table to translate the text.

First, we create an alphabet string, and then create a cipher using string slicing.

```python
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = alphabet[key:] + alphabet[:key]
```

For example:

> if `key = 3`

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher   = "defghijklmnopqrstuvwxyzabc"
```

> if `key = -2`

```python
alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher   = "yzabcdefghijklmnopqrstuvwx"
```

Then, make the mapping table using the `maketrans()` method.

```python
    mapping_table = str.maketrans(alphabet + alphabet.upper(), cipher + cipher.upper())
```

Note: the use of `.upper()` enables the function to encrypt uppercase letters as well.

So the mapping table is actually mapping both the lowercase and uppercase letters.

> if `key = 3`

```python
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher   = "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC"
```

Finally, use the `translate()` method to translate the text.

```python
    return text.translate(mapping_table)
```

The `translate()` method uses the mapping table to translate the text.  
So every `a` is replaced with `d`, `b` with `e`, `c` with `f`, and so on.

#### Sample Output for `encrypt_text()`

```python
text = "hallo"
print(text)
print(encrypt_text(text, 3))
```

```console
hallo
kdoor
```

### `encrypt_text_loop_version()`, explained

This function uses a for loop to iterate through every character in the text.  
This function basically does the same as the previous encrypt_text() function, but instead this time:

1. Iterate through every character in the text.
2. If the character is a letter, encrypt it.
3. If the character is not a letter, leave it as it is.

```python
    for c in text:
        if c.isalpha():
            index = alphabet.index(c.lower())
            if c.isupper():
                encrypted_text += cipher[index].upper()
            else:
                encrypted_text += cipher[index]
        else:
            encrypted_text += c
```

Note: I do not use this function in the program since I already know that the `maketrans()` and `translate()` methods exist. This function is just a more educational version of the previous function `encrypt_text()`.

#### Sample Output for `encrypt_text_loop_version()`

```python
text = "hallo"
print(text)
print(encrypt_text(text, 3))
```

```console
hallo
kdoor
```

### `menu()`, explained

This function just prints the menu and asks the user for a choice.

```python
def menu() -> int:
    print(
        "\n"
        "==========================\n",
        "[1] Enter Lists of Text/s \n",
        "[2] Encrypt               \n",
        "[3] View Encrypted        \n",
        "[4] Exit                  ",
    )

    return int(input("Enter Choice: "))
```

### `enter_text()`, explained

This function allows the user to enter multiple text and add it to the list of text to be encrypted.

First, we want to clear all lists.  
This is because every time we add new text, the previous text should be overridden.  
So we clear all lists first to remove all the text and the previous encrypted text if there is any.

```python
    t_lst.clear()
    enc1.clear()
    enc2.clear()
```

Then, we ask the user for the number of text inputs.

```python
    num_of_inputs = int(input("Number of text inputs: "))
```

Then, we use a for loop to ask the user for the text inputs and add it to the text list.

```python
    for i in range(num_of_inputs):
        element = input(f"[{i + 1}] ")
        t_lst.append(element)
```

We then return all three lists, this is because we want to override the previous lists with the new lists.

```python
    return [t_lst, enc1, enc2]
```

Note: we are returning only one list with the three lists inside of it. To separate the lists, we can use either indexing or multiple assignment. Multiple assignment is used in this case, as seen in the main program loop.

```python
if choice == 1:
        text_list, encrypted_1, encrypted_2 = enter_text(text_list, encrypted_1, encrypted_2)
```

This assigns `t_lst` to `text_list`, `enc1` to `encrypted_1`, and `enc2` to `encrypted_2`.

### `encrypt()`, explained

This function encrypts the text in the list of text in two levels.

First, we check if there is any text in the list of text.  
If there is no text, we print a message and immediately return the two encrypted text lists to break out of the function.

```python
    if len(t_lst) == 0:
        print("Enter list of text first.")
        return [enc1, enc2]
```

If there is text to be encrypted, we clear the two encrypted text lists.  
This is because a user can encrypt a text multiple times, and we want to clear the previous encrypted text.

```python
    enc1.clear()
    enc2.clear()
```

Then, we ask the user for the two keys.

```python
    key1 = int(input("First Level Shift: "))
    key2 = int(input("Second Level Shift: "))
```

Then, we check if the keys are greater than 26 or less than -26.  
If so, we use conditionals to get the remainder of the key divided by 26.

```python
    if key1 > 26 or key1 < -26:
        key1 = key1 % 26
    if key2 > 26 or key2 < -26:
        key2 = key2 % 26
```

Then, we use a for loop to encrypt the text in the list of text using the first key.

```python
    for text in t_lst:
        enc_text_1 = encrypt_text(text, key1)
        enc1.append(enc_text_1)
```

Then, we use a for loop to encrypt the text in enc1 using the second key.

```python
    for text in enc1:
        enc_text_2 = encrypt_text(text, key2)
        enc2.append(enc_text_2)
```

Finally, we return the two encrypted text lists.

```python
    return [enc1, enc2]
```

Again, since the function returns a list with the two lists inside of it, we use multiple assignment to assign the two lists to the two encrypted text lists.

```python
    elif choice == 2:
        encrypted_1, encrypted_2 = encrypt(text_list, encrypted_1, encrypted_2)
```

This assigns `enc1` to `encrypted_1` and `enc2` to `encrypted_2`.

### `view_encrypted()`, explained

This function allows the user to see the encryption process.

First, we check if there is any text in the list of text.

```python
    if len(enc1) == 0 or len(enc2) == 0:
        print("No ciphered text yet!")
```

If there is text, we use a for loop to print the text, the first level encrypted text, and the second level encrypted text.

```python
    else:
        for i in range(len(t_lst)):
            print(f"[{i+1}] {t_lst[i]} ===> {enc1[i]} ===> {enc2[i]}")
```

For example, this is the output where:

```python
t_lst = ["hallo", "world"]

# encrypted to the first level by 3
enc1  = ["kdoor", "zruog"]

# encypted to the second level by -2
enc2  = ["ibmmp", "xpsme"]
```

```console
Enter Choice: 3
[1] hallo ===> kdoor ===> ibmmp
[2] world ===> zruog ===> xpsme
```

This function does not return anything, it just prints the text.

### Main Program, explained

The main program starts by initializing the needed variables.

```python
text_list = []
encrypted_1 = []
encrypted_2 = []
```

Then the main program loop starts.

```python
RUNNING = True
while RUNNING:
    choice = menu()
    if choice == 1:
        text_list, encrypted_1, encrypted_2 = enter_text(text_list, encrypted_1, encrypted_2)

    elif choice == 2:
        encrypted_1, encrypted_2 = encrypt(text_list, encrypted_1, encrypted_2)

    elif choice == 3:
        view_encrypted(text_list, encrypted_1, encrypted_2)

    elif choice == 4:
        RUNNING = False
        print("Bye!")

    else:
        print("Invalid choice!")
```

The main program loop only does the following.

1. Prints the menu which asks for the user’s choice, which is then assigned to the variable `choice`.
2. Check the `choice` variable using conditionals.
3. Proceed to the function/code block depending on the `choice` variable.

If the choice is invalid, the program prints a message and loops back to the menu, since `RUNNING` is still `True`.

```python
    else:
        print("Invalid choice!")
```

The program only exits the loop if the choice is 4, which is to exit the program, and since `RUNNING` is set to `False`, the while loop can no longer run.

```python
    elif choice == 4:
        RUNNING = False
        print("Bye!")
```
