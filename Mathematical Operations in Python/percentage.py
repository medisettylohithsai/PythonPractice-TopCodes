"""**Percentage Calculation:**
    - Write a program that calculates the percentage of a given number.
"""
number = float(input("Enter the number: "))
percentage = float(input("Enter the percentage: "))

result = (percentage / 100) * number

print(f"{percentage}% of {number} is {result}")