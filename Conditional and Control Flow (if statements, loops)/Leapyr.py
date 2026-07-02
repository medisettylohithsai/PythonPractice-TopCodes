#Develop a program that checks if a year is a leap year.
n=int(input())
if (n%400==0) or (n%100!=0 and n%4==0):
    print(" leap ")
else:
    print("not Leap")