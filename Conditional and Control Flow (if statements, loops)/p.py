# Create a program that uses a loop to print the first 10 multiples of 4.
num = int(input("Enter the number: "))
count = int(input("Enter how many multiples: "))

for i in range(1, count + 1):
    print(num * i)