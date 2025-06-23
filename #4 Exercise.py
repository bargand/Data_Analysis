x= int(input("First Number: "))
y= int(input("First Number: "))
z= input("give operator")

if (z=="+"):
    print(x+y)
elif (z=="-"):
    print(x-y)
elif (z=="*"):
    print(x*y)
elif (z=="**"):
    print(x**y)
elif (z=="/"):
    print(x/y)
elif (z=="//"):
    print(x//y)
elif (z=="%"):
    print(x%y)
else:
    print("It is invalid Operator")


#or
'''
x= int(input("First Number: "))
y= int(input("First Number: "))
z= input("give operator")

operators={
    "+": x+y,
    "-": x-y,
    "/": x/y,
    "*": x*y,
    "**": x**y,
    "//": x//y,
    "%": x%y
}

print(operators)
'''