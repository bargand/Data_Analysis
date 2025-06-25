
#Some if else exercise

'''
#Even or Odd

num = int(input("Enter your number: "))

if ((num%2) == 0):
    print("this is a even number")
else:
    print("this is a odd number")

'''

'''
#Positive, Negative, or Zero

num2 = float(input("enter your random number: "))

if (num2<0):
    print("Negative")
elif(num2>0):
    print("Positive")
else:
    print("Zero")

'''

'''
#Age Check

age = int(input("Enter your age: "))

if(age >= 18):
    print("You acn drive")
elif(age <= 18):
    print("You can not drive")
else:
    print("please enter a valid number")

'''

'''
#Number Comparison

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

if (num3 > num4):
    print("first number is greater than second number")
elif(num3 < num4):
    print("first number is lesser than second number")
else:
    print("first and second number is equal")

'''

'''
#Grade Checker

result = int(input("Enter your number: "))

if (90<= result >= 100):
    print("Grade A")
elif(80<= result <= 89):
    print("Grade B")
elif(70<= result <= 79):
    print("Grade C")
elif(60<= result <= 69):
    print("Grade D")
elif(result <= 59):
    print("FAIL")
else:
    print("Enter a valid number")

'''

#Nested if else

'''
#Number Sign and Type(first check it is positive, negetive or zero, then it check if it is possitive so it is even or odd)

a = int(input("Enter your number: "))

if (a > 0):
    print("it is positive number")
    if((a%2) == 0):
        print("it is even number")
    else:
        print("it is odd number")
elif(a < 0):
    print("it is negetive number")
else:
    print("it is zero")

'''

'''
#Password Checker

user = "bargand"
passw = 12345

userInput = input("Enter your usernam: ")
passwInput = int(input("Enter your passward: "))

if (userInput == user):
    print("username is correct")
    if(passwInput == passw):
        print("successfully loggedin")
    else:
        print("incorrect passward")
else:
    print("username is incorrect")

'''

#Largest of Three Numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (b <= a >= c):
    if(a==b==c):
        print("all 3 numbers are same")
    elif(a==b):
        print("a and b is same number")
    elif(a==c):
        print("a and c is same number")
    else:
        print("a is largest")
elif(a < b > c):
    if(b==a):
        print("b and a is same number")
    elif(b==c):
        print("b and c is same number")
    else:
        print("b is largest")
elif(a < c > b):
    if(c==a):
        print("c and a is same number")
    elif(c==b):
        print("c and b is same number")
    else:
        print("c is largest")
else:
    print("Do not understand your numbers")
