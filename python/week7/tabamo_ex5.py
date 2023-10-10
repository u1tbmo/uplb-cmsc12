"""
This program encrypts a list of text using Caesar’s Cipher in two levels.
"""
# Exercise 5 - Tabamo, Euan Jed S. - Oct 10, 2023

text_list = []
encrypted_1 = []
encrypted_2 = []


def encrypt_text(text, key):
    """ This function encrypts text using a key.

    Arguments:
        text (str) - the text to be encrypted
        key (int) - the rotational key for the cypher
    
    Returns:
        (str) - the encrypted text
    """
    # This function uses the maketrans() and translate() methods for strings
    # maketrans() - https://www.w3schools.com/python/ref_string_maketrans.asp
    # translate() - https://www.w3schools.com/python/ref_string_translate.asp
    # Already solved by me previously before this exercise was given.
    # https://exercism.org/tracks/python/exercises/rotational-cipher/solutions/u1tbmo

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # cipher is the rotated alphabet using the key
    cipher = alphabet[key:] + alphabet[:key]
    # create a mapping table, mapping the alphabet to the cipher
    mapping_table = str.maketrans(alphabet + alphabet.upper(), cipher + cipher.upper())
    # returns the translated text
    return text.translate(mapping_table)

def menu() -> int:
    """ This function prints a menu and asks the user for a choice.

    Returns:
        (int) - the choice
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

def enter_text(t_lst, lst1, lst2) -> list:
    """ This function allows the user to create a list of text and add it to the lis.

    Args:
        t_lst (list): the list of text
        lst1 (list): the list of first level encrypted text
        lst2 (list): the list of second level encrypted text

    Returns:
        list: the list of text
    """

    # Clear the lists
    t_lst.clear()
    lst1.clear()
    lst2.clear()

    # Ask the user how many text they want to add
    num_of_inputs = int(input("How many do you want to add?\n >>> "))

    # Ask the user for the text num_of_inputs times
    for i in range(num_of_inputs):
        element = input(f"[{i + 1}] ")
        t_lst.append(element.lower())

    return t_lst


def encrypt(t_lst, lst1, lst2) -> list:
    """ This function encrypts the text_list.

    Args:
        t_lst (list) - the list of text to be encrypted
        lst1 (list) - the list to store first level encrypted text
        lst2 (list) - the list to store second level encrypted text

    Returns:
        list - the first level and second level encrypted text
    """
    # Check if the text list has text.
    if len(t_lst) == 0:
        print("Enter list of text first.")
        return [lst1, lst2]

    # Clear the encrypted text lists
    lst1.clear()
    lst2.clear()

    key1 = int(input("First Level Shift: "))
    key2 = int(input("Second Level Shift: "))

    # Encrypt to the first level by calling encrypt_text()
    for text in t_lst:
        enc_text_1 = encrypt_text(text, key1)
        lst1.append(enc_text_1)

    # Encrypt to the second level by calling encrypt_text()
    for text in lst1:
        enc_text_2 = encrypt_text(text, key2)
        lst2.append(enc_text_2)

    # return the encrypted text lists
    return [lst1, lst2]


def view_encrypted(t_lst, lst1, lst2) -> None:
    """ This function allows the user to see the encryption process.

    Args:
        t_lst (list) - the list of text to be encrypted
        lst1 (list) - the list of first level encrypted text
        lst2 (list) - the list of second level encrypted text
    """
    # Check if the encrypted text lists have encrypted text.
    if len(lst1) == 0 or len(lst2) == 0:
        print("No ciphered text yet!")
        
    else:
        for i, text in enumerate(t_lst):
            print(f"[{i+1}] {text} ===> {lst1[i]} ===> {lst2[i]}")

# main program loop
RUNNING = True
while RUNNING:
    choice = menu()
    if choice == 1:
        text_list = enter_text(text_list, encrypted_1, encrypted_2)
    elif choice == 2:
        # since encrypt() returns a list, we can unpack the list into their respective lists
        encrypted_1, encrypted_2 = encrypt(text_list, encrypted_1, encrypted_2)
    elif choice == 3:
        view_encrypted(text_list, encrypted_1, encrypted_2)
    elif choice == 4:
        RUNNING = False
        print("See you soon!")
    else:
        print("Invalid choice!")