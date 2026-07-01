# 19. **Hypotenuse Calculation:**
#     - Develop a program that uses the Pythagorean theorem to find the hypotenuse of a right-angled triangle.

import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))

c = math.sqrt(a**2 + b**2)

print(f"Hypotenuse = {c}")