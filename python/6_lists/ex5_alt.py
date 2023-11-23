# create a string of the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

text_list = []
encrypted_1 = []
encrypted_2 = []

def encrypt_text(text, key) -> str:
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

# Main Program Loop
RUNNING = True
while RUNNING:
    print(
        "\n"
        "==========================\n",
        "[1] Enter Lists of Text/s \n",
        "[2] Encrypt               \n",
        "[3] View Encrypted        \n",
        "[4] Exit                  ",
    )

    choice = int(input("Enter Choice: "))

    if choice == 1:
        # Reset the lists when we enter new text
        text_list.clear()
        encrypted_1.clear()
        encrypted_2.clear()

        # Ask the user how many text they want to add
        num_of_inputs = int(input("Number of text inputs: "))

        # Ask the user for the text num_of_inputs times
        for i in range(num_of_inputs):
            element = input(f"[{i + 1}] ")
            text_list.append(element)

    elif choice == 2:
        # Check if the text list has text, if not, return the encrypted text lists as is
        if len(text_list) == 0:
            print("Enter list of text first.")

        else:
            # Clear the encrypted text lists
            encrypted_1.clear()
            encrypted_2.clear()

            key1 = int(input("First Level Shift: "))
            key2 = int(input("Second Level Shift: "))

            # since the key can be any integer, we need to make sure that it is within the range of -26 to 26
            if key1 > 26 or key1 < -26:
                key1 = key1 % 26
            if key2 > 26 or key2 < -26:
                key2 = key2 % 26

            # Encrypt to the first level by calling encrypt_text()
            for text in text_list:
                enc_text_1 = encrypt_text(text, key1)
                encrypted_1.append(enc_text_1)

            # Encrypt to the second level by calling encrypt_text()
            for text in encrypted_1:
                enc_text_2 = encrypt_text(text, key2)
                encrypted_2.append(enc_text_2)

    elif choice == 3:
        # Check if the encrypted text lists have encrypted text.
        if len(encrypted_1) == 0 or len(encrypted_2) == 0:
            print("No ciphered text yet!")
        
        else:
            # iterate through text_list, encrypted_1, and encrypted_2 using range(len(lst))
            # and print the text, encrypted_1, and encrypted_2 side by side
            for i in range(len(text_list)):
                print(f"[{i+1}] {text_list[i]} ===> {encrypted_1[i]} ===> {encrypted_2[i]}")

    elif choice == 4:
        RUNNING = False
        print("Bye!")

    else:
        print("Invalid choice!")
