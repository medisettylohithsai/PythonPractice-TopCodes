"""**Trigonometric Functions:**
    - Write a program that uses the `math` module to calculate the sine and cosine of an angle
"""

import math

angle = float(input("Enter angle in degrees: "))

# Convert degrees to radians
radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

# Reciprocal functions
cosec_value = 1 / sin_value if sin_value != 0 else "Undefined"
sec_value = 1 / cos_value if cos_value != 0 else "Undefined"
cot_value = 1 / tan_value if tan_value != 0 else "Undefined"

print("sin =", sin_value)
print("cos =", cos_value)
print("tan =", tan_value)
print("cosec =", cosec_value)
print("sec =", sec_value)
print("cot =", cot_value)