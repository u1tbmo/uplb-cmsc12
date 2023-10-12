"""
This program encrypts a list of text using Caesar’s Cipher in two levels.
"""
# Exercise 5 - Tabamo, Euan Jed S. - Oct 10, 2023

text_list = []
encrypted_1 = []
encrypted_2 = []


def encrypt_text(text, key) -> str:
    """This function encrypts text using a key.

    This version uses the maketrans() and translate() methods for strings.

    Arguments:
        text (str) - the text to be encrypted
        key (int) - the rotational key for the cypher
    
    Returns:
        str - the encrypted text
    """

    # maketrans() - https://www.w3schools.com/python/ref_string_maketrans.asp
    # translate() - https://www.w3schools.com/python/ref_string_translate.asp

    # Already solved by me previously before this exercise was given.
    # https://exercism.org/tracks/python/exercises/rotational-cipher/solutions/u1tbmo

    # create a string of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # create a rotated alphabet using the key by using string slicing
    cipher = alphabet[key:] + alphabet[:key]
    
    # create a mapping table, mapping the alphabet to the cipher
    # .upper() is used to include uppercase letters in the cipher, so that the cipher can be used for uppercase letters as well
    # translate() only translates characters that are in the mapping table, therefore, characters that are not in the alphabet are not encrypted
    mapping_table = str.maketrans(alphabet + alphabet.upper(), cipher + cipher.upper())

    # returns the translated text
    return text.translate(mapping_table)

# This is an alternative solution to encrypt_text() using a loop,
# though it is not used in the main program loop below,
# it is left as a comment since it is a valid solution that does not use maketrans() and translate()
def encrypt_text_loop_version(text, key) -> str:
    """This function encrypts text using a key.

    This version uses a for loop to iterate through every character in the text.

    Arguments:
        text (str) - the text to be encrypted
        key (int) - the rotational key for the cypher
    
    Returns:
        str - the encrypted text
    """

    # create a string of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # create a rotated alphabet using the key by using string slicing
    cipher = alphabet[key:] + alphabet[:key]
    
    # create an empty string to store the encrypted text
    encrypted_text = ''

    # iterate through every character in the text
    for c in text:
        # if the character is a letter, encrypt it
        if c.isalpha():
            # find the index of the character in the alphabet
            index = alphabet.index(c.lower())

            # if the character is uppercase, add the uppercase cipher letter to the encrypted text
            # this makes the cipher usable for uppercase letters as well
            if c.isupper():
                encrypted_text += cipher[index].upper()
            else:
                encrypted_text += cipher[index]

        # if the character is not a letter, add it to the encrypted text as is
        else:
            encrypted_text += c

    return encrypted_text


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


def enter_text(t_lst, enc1, enc2) -> list:
    """This function allows the user to create a list of text and add it to the list.

    Args:
        t_lst (list): the list of text
        enc1 (list): the list of first level encrypted text
        enc2 (list): the list of second level encrypted text

    Returns:
        list: the list of the three lists
    """

    # Reset the lists when we enter new text
    t_lst.clear()
    enc1.clear()
    enc2.clear()

    # Ask the user how many text they want to add
    num_of_inputs = int(input("Number of text inputs: "))

    # Ask the user for the text num_of_inputs times
    for i in range(num_of_inputs):
        element = input(f"[{i + 1}] ")
        t_lst.append(element)

    # Return all the lists
    return [t_lst, enc1, enc2]


def encrypt(t_lst, enc1, enc2) -> list:
    """This function encrypts the text in the list of text in two levels.

    Args:
        t_lst (list): the list of text
        enc1 (list): the list of first level encrypted text
        enc2 (list): the list of second level encrypted text

    Returns:
        list: the list of both encrypted text lists
    """

    # Check if the text list has text, if not, return the encrypted text lists as is
    if len(t_lst) == 0:
        print("Enter list of text first.")
        return [enc1, enc2]

    # Clear the encrypted text lists
    enc1.clear()
    enc2.clear()

    key1 = int(input("First Level Shift: "))
    key2 = int(input("Second Level Shift: "))

    # since the key can be any integer, we need to make sure that it is within the range of -26 to 26
    if key1 > 26 or key1 < -26:
        key1 = key1 % 26
    if key2 > 26 or key2 < -26:
        key2 = key2 % 26

    # Encrypt to the first level by calling encrypt_text()
    for text in t_lst:
        enc_text_1 = encrypt_text(text, key1)
        enc1.append(enc_text_1)

    # Encrypt to the second level by calling encrypt_text()
    for text in enc1:
        enc_text_2 = encrypt_text(text, key2)
        enc2.append(enc_text_2)

    # return the encrypted text lists in a list
    return [enc1, enc2]


def view_encrypted(t_lst, enc1, enc2) -> None:
    """This function allows the user to see the encryption process.
    """

    # Check if the encrypted text lists have encrypted text.
    if len(enc1) == 0 or len(enc2) == 0:
        print("No ciphered text yet!")
        
    else:
        # iterate through t_lst, enc1, and enc2 using range(len(lst))
        # and print the text, enc1, and enc2 side by side
        for i in range(len(t_lst)):
            print(f"[{i+1}] {t_lst[i]} ===> {enc1[i]} ===> {enc2[i]}")
        

# Main Program Loop
RUNNING = True
while RUNNING:
    choice = menu()
    if choice == 1:
        # # since enter_text() returns a list of three lists, we can access the lists using indexing
        
        # lists = enter_text(text_list, encrypted_1, encrypted_2)
        # text_list = lists[0]
        # encrypted_1 = lists[1]
        # encrypted_2 = lists[2]

        # better alternative: since enter_text() returns a list of three lists
        # we can use multiple assignment to assign the lists to the variables
        text_list, encrypted_1, encrypted_2 = enter_text(text_list, encrypted_1, encrypted_2)

    elif choice == 2:
        # # since encrypt() returns a list of two lists, we can access the lists using indexing
        # lists = encrypt(text_list, encrypted_1, encrypted_2)
        # encrypted_1 = lists[0]
        # encrypted_2 = lists[1]

        # better alternative: since encrypt() returns a list of two lists
        # we can use multiple assignment to assign the lists to the variables
        encrypted_1, encrypted_2 = encrypt(text_list, encrypted_1, encrypted_2)

    elif choice == 3:
        view_encrypted(text_list, encrypted_1, encrypted_2)

    elif choice == 4:
        RUNNING = False
        print("Bye!")

    else:
        print("Invalid choice!")
