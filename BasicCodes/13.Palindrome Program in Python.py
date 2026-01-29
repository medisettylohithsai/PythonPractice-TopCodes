#Palindrome Program in Python
n=int(input())
s=(str(n)[::-1])
print(s)
if s==str(n):
    print("Palindrom number")
else:
    print("Not palindrome number")
