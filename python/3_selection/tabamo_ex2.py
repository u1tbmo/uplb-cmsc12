"""This program helps in deciding where a student can eat using a few characteristics."""
# Exercise 2 - Tabamo, Euan Jed S.

# Initialize variable/s
recommendation = ""

# 1. Allow the user to specify what type of establishment they would want to eat at.
# The only available choices for this should be “RESTAURANT”, “FAST FOOD”, “HOMEMADE”
establishment_type = input(
    "What type of establishment would you "
    "like to eat in?"
    "\nChoose one: [RESTAURANT, FAST FOOD, HOMEMADE]"
    "\n> "
    )

# Normalize to uppercase
establishment_type = establishment_type.strip().upper()

# Check if the establishment_type is valid
if ((establishment_type == "RESTAURANT") or
    (establishment_type == "FAST FOOD") or
    (establishment_type == "HOMEMADE")):
    pass
else:
    print("ValueError: Establishment type is invalid.")
    exit()

# 2. Allow the user to specify how many people they will be dining with.
people_quantity = int(input(
    "How many people are in the group including you?"
    "\n> "
))

# Raise an error if people_quantity < 1 and terminate
if people_quantity < 1:
    print("ValueError: Input must be at least one.")
    exit()

# Find the correct recommendation depending on people_quantity and establishment_type
if 1 <= people_quantity <= 3:
    if establishment_type == "RESTAURANT":
        recommendation = "Dalcielo"
    elif establishment_type == "FAST FOOD":
        recommendation = "McDonald's"
    else:
        recommendation = "Along Glo's"
else:
    if establishment_type == "RESTAURANT":
        recommendation = "Bonitos"
    elif establishment_type == "FAST FOOD":
        recommendation = "Jollibee"
    else:
        recommendation = "Cadapan's"

# 3. Show the user a recommendation for a place to eat
# using the characteristics they have specified.

if people_quantity == 1:
    print(f"If you are eating by yourself, I recommend {recommendation}.")
elif people_quantity == 2:
    print(f"With a partner, friend, or bestie? I recommend {recommendation}.")
elif people_quantity == 3:
    print(f"With a small group like that, I recommend {recommendation}.")
else:
    print(f"With a group of {people_quantity}, I recommend {recommendation}.")
