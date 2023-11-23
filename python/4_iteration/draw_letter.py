"""Creates a letter L based on input"""
# Tabamo, Euan Jed S. - Sep 26

# Get input
l_length = int(input("Enter dimension: "))

# Draw vertical
for row in range (l_length - 1):
    print("*")

# Draw horizontal
print(("* " * l_length).strip()) # .strip() removes the extra space at the end
