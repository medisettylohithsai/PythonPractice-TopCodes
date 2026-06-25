import calendar

# Take input from the user
year = int(input("Enter a year: "))

# Using the built-in library function
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
