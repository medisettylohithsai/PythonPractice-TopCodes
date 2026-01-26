a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("a is greater than both b and c")
elif b>c:
    print("b is greater than both a and c")
else:
    print("c is greater than both a and b")