"""This program calculates the BMI and determines 
its classification given the weight (in kg) and 
height (in meters) of a person."""
# Exercise 2 - Submitted by Tabamo, Euan Jed S.

# Get inputs, weight and height
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate the BMI
bmi = round(weight / (height ** 2), 2)

# Assign a classification depending on the BMI
if bmi < 18.5:
    CLASSIFICATION = "Underweight"
elif 18.5 <= bmi < 25:
    CLASSIFICATION = "Normal"
elif 25 <= bmi < 30:
    CLASSIFICATION = "Overweight"
else:
    CLASSIFICATION = "Obese"

# Print output
print("")
print(f"BMI: {bmi}")
print(f"Classification: {CLASSIFICATION}")
