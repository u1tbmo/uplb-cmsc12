"""
Introduction to Dictionaries
"""

subjects = {
    "CMSC":"Computer Science",
    "MATH":"Mathematics",
    "STAT":"Statistics",
    "PHYS":"Physics"
}
print("---------------------")

for k,v in subjects.items():
    print(f"{k}\t{v}")

print("---------------------")

# subjects.keys() is unnecessary since iterating through the dictionary iterates through the keys
for k in subjects:
    print(f"{k}")

print("---------------------")


for v in subjects.values():
    print(f"{v}")

print("---------------------")

# Lists in Dictionaries

UPMBT = {
    # jersey number (keys): [name (0), pos (1), age (2), height (3)] (values)
    13:["JD Cagulangan", "G", 21, 175],
    18:["Harold Alarcon", "G", 21, 185],
    77:["Chicco Briones", "G", 21, 185],
    17:["Lebron Lopez", "F", 20, 198],
    27:["CJ Cansino", "G", 23, 188],
}

print(f"{UPMBT[77][0]} is the player wearing jersey number 77.")
print(f"{UPMBT[27][2]} is the age of {UPMBT[27][0]}.")

print("---------------------")

for v in UPMBT.values():
    print(f"{v[0]}\t {v[2]}")
