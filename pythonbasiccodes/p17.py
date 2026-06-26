#Develop a program that converts a given number to a binary representation.
num = int(input("Enter a number: "))

binary = (bin(num)[2 :])

print("Binary representation:", binary)