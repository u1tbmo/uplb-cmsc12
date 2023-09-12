"""This program will show the financial impact of sustaining one's milk tea buying habit."""
# Exercise 1 - Submitted by Tabamo, Euan Jed S.

### DECLARE CONSTANT VARIABLE
INTEREST_RATE = 0.04

### INPUTS
# GOAL 1: Allow the user to specify their milk tea buying frequency in a week.
weekly_milk_tea_quantity = input("How many times do you buy milk tea per week?\n > ")
# GOAL 2: Allow the user to specify the price of their usual milk tea order.
milk_tea_cost = input("How much does a milk tea typically cost?\n > ")

### CONVERSION
# Convert input from string to int
weekly_milk_tea_quantity = int(weekly_milk_tea_quantity)
# Using float instead of int allows for prices with cents
milk_tea_cost = float(milk_tea_cost)

### COMPUTATION
# Calculates how much money is spent per year on milk tea
periodic_deposit = milk_tea_cost * (weekly_milk_tea_quantity * 52)

periodic_deposit1 = periodic_deposit * 1
periodic_deposit5 = periodic_deposit * 5
periodic_deposit10 = periodic_deposit * 10
periodic_deposit20 = periodic_deposit * 20
periodic_deposit40 = periodic_deposit * 40

# Calculates the future value if the money is saved in a bank with a high-yield.
future_value1 = periodic_deposit * ((((1 + INTEREST_RATE)**1) - 1) / INTEREST_RATE)
future_value5 = periodic_deposit * ((((1 + INTEREST_RATE)**5) - 1 )/ INTEREST_RATE)
future_value10 = periodic_deposit * ((((1 + INTEREST_RATE)**10) - 1) / INTEREST_RATE)
future_value20 = periodic_deposit * ((((1 + INTEREST_RATE)**20) - 1) / INTEREST_RATE)
future_value40 = periodic_deposit * ((((1 + INTEREST_RATE)**40) - 1) / INTEREST_RATE)

# Rounds the future values to two digits.
future_value1 = round(future_value1, 2)
future_value5 = round(future_value5, 2)
future_value10 = round(future_value10, 2)
future_value20 = round(future_value20, 2)
future_value40 = round(future_value40, 2)

### OUTPUTS
print("") # line spacing

# GOAL 3: Show the user how much they will be spending on milk tea per year.
print(f"The total amount of money you would have spent on milk tea per year is {periodic_deposit}.")
print("") # line spacing

# GOAL 4: Show the user the saving vs. spending impact of
# their habit using 1, 5, 10, 20, and 40 year timeframes.
print(f"If you saved this money every year in a high-yield bank account\n"
      f"earning {INTEREST_RATE*100}% APY, you would have earned an extra:")
print(f" > Php {future_value1} in 1 year (vs spending Php {periodic_deposit1})")
print(f" > Php {future_value5} in 5 years (vs spending Php {periodic_deposit5})")
print(f" > Php {future_value10} in 10 years (vs spending Php {periodic_deposit10})")
print(f" > Php {future_value20} in 20 years (vs spending Php {periodic_deposit20})")
print(f" > Php {future_value40} in 40 years (vs spending Php {periodic_deposit40})")
