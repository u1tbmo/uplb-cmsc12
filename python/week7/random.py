key = 3
# create a string of the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# create a rotated alphabet using the key by using string slicing
cipher = alphabet[key:] + alphabet[:key]
print(f"{alphabet}")
print(f"{cipher}")