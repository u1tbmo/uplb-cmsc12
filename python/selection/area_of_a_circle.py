""" This program computes the area of a circle given its radius."""

# Made by Euan Jed Tabamo

# Import math library
import math

# Declare constants
pi = round(math.pi, 2) # get the value of pi directly from math library, round to 2 digits.

# Ask for input
radius = input("What is the radius of the circle?\n > ") # ask for the radius from the user
radius = int(radius) # type cast to int

# Print the result

circle_area = pi * (radius ** 2) # compute the circle_area
print(f"The area of the circle with radius {radius} is {circle_area}.") # print using f-strings
