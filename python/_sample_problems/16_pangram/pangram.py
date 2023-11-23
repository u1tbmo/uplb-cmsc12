def ispangram(s: str) -> bool:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in s.lower():
            return False
    return True
