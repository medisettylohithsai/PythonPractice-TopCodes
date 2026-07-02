#Write a program that prints the multiplication table of a given number up to 10.
n=int(input())
for i in range(11):
    print(n,"*",i,"=",n*i)