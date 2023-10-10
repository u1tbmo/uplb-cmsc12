grade_list = [
    ["Input/Output", 100],
    ["Conditionals", 90],
    ["Iteration", 80],
    ["Functions", 70],
]

# print every item and grade for each item
for item in grade_list:
    print(f"{item[0]}: {item[1]}")

# compute the AVERAGE
grade_sum = 0
for item in grade_list:
    grade_sum += item[1]

AVERAGE = round(grade_sum / len(grade_list), 2)

print(f"Your average is: {AVERAGE}")
