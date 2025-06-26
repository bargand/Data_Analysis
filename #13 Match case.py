'''
x = int(input("enter your number between 0-5: "))

match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")
    case _ if(x!=90):
        print("x is not 90")
    case _ if(x!=80):
        print("x is not 80")
    case _:
        print("number us not in 1-5")

'''

'''
#Exercise 1: Weekday Mapper(Write a program that takes a number (1–7) as input and uses match-case to print the corresponding weekday.)

day = int(input("Enter weekday number: "))

match day:
    case 1:
        print("MONDAY")
    case 2:
        print("TUE")
    case 3:
        print("wed")
    case 4:
        print("thr")
    case 5:
        print("fri")
    case 6:
        print("sat")
    case 7:
        print("sun")
    case _:
        print("your input weekday number is not in 1-7")

'''

'''
#Exercise 2: Basic Calculator(Create a program that takes two numbers and an operator (+, -, *, /) as input, then uses match-case to perform the correct operation.)

num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
ind= input("Enter Operator: ")

match ind:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print('you give a wrong operator, please input (+, -, *, /) this operators')

'''

'''
#Exercise 3: Grade Checker(Write a program that takes a letter grade (A, B, C, D, F) and uses match-case to print a message about performance.)
'''

'''
#Exercise 3: Grade Checker(Write a program that takes a letter grade (A, B, C, D, F) and uses match-case to print a message about performance.)

grade = input("Enter your grade(e.g O, A+, A, B+, B, C, D, F): ")

match grade:
    case "O":
        print("Outstanding")
    case "A+":
        print("Excellent")
    case "A":
        print("Very good")
    case "B+":
        print("Good")
    case "B":
        print("About Average")
    case "C":
        print("Average")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("your gade is not under(e.g O, A+, A, B+, B, C, D, F)")

'''

'''
#Exercise 4: Shape Identifier

day = int(input("Enter number of sides of your shape: "))

match day:
    case 3:
        print("Triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case _:
        print("invalid number of sides of your shape")

'''

'''
#Exercise 5: Tuple Matching(Write a program that accepts a tuple like (action, object) and uses match to determine the result.)

command = ("move", "left")

match command:
    case ("move", "left"):
        print("Moving left")
    case ("move", "right"):
        print("Moving right")
    case ("jump", "up"):
        print("Jumping up")
    case ("duck", "down"):
        print("Ducking down")
    case _:
        print("Unknown command")

'''

'''
#Exercise 6: HTTP Status Code Checker(Use match to interpret HTTP status codes (e.g., 200, 404, 500).)
'''

https = int(input("Enter HTTPS status: "))

match https:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("not a valid https status")