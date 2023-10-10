"""
This program takes an input string and changes prints the string with all As replaced with Os.
"""

input_str = input("Enter string: ")

result = ""

for c in input_str:
    if c == "a":
        result += "o"
    elif c == "A":
        result += "O"
    else:
        result += c

print(f"New String: {result}")
