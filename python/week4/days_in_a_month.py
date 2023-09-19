"""Gets the number of days of a month."""
# Tabamo, Euan Jed S.

month = input("Enter 3-letter month: ")

# normalize to lowercase and remove whitespace, slice the string to three characters.
month = month.lower().strip()[0:3]

if ((month == "jan") or (month == "mar") or (month == "may") or (month == "jul")
    or (month == "aug") or (month == "oct") or (month == "dec")):
    print("Number of days: 31")
elif (month == "apr") or (month == "jun") or (month == "sep") or (month == "nov"):
    print("Number of days: 30")
elif month == "feb":
    print("Number of days: 28")
else:
    print("Invalid Input")
