""" This program computes the area of a circle given its radius."""

# Made by Euan Jed Tabamo

# Import math library
import math

# Declare constants
pi = round(math.pi, 2)

# Ask for input
radius = input("What is the radius of the circle?\n > ")
radius = int(radius)

# Print the result

circle_area = pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is {circle_area}.")
