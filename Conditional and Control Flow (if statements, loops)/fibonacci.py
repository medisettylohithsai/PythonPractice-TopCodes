#Write a program that prints the Fibonacci sequence up to the 15th term.
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
n=int(input())
fibonacci(n)