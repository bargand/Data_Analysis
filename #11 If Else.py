
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