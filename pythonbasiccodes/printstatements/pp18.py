"""**Print with File Parameter:**
    - Write a program that prints to a file using the `file` parameter in the `print` function.
"""

file = open("output.txt", "w")

print("Hello, Python!", file=file)

file.close()