'''
#countdown timer

sec = 10

while (sec > 0):
    print(f"{sec} sec remaining")
    sec -= 1
else:
    print("Times Up")

'''

'''
#Password Retry System

password = "Tubai1234"

remaining_try = 5

while remaining_try > 0:
    user_input = str(input("Enter Your Password: "))
    if (password == user_input):
        print("Successfully loggedin")
        break
    else:
        remaining_try -= 1
        print(f"not a valid password and you have {remaining_try} remaining try")
        if remaining_try == 0:
            print("Too many attempt you did account is freeze for 12 hrs")
    
'''


'''
password = "Tubai1234"
user_input = ""

while user_input != password:
    user_input = str(input("Enter your password: "))
print("access granted")

'''

'''
#User Menu Until Exit (Show a menu (1. Add, 2. Subtract, etc.). Keep asking the user to choose an option until they pick “Exit”. Use a while loop to repeat the menu.)

menu_list = []

exitt = "no"
menu = ""

while exitt != menu_list:
    menu = str(input("Enter your menu item: "))
    if menu == "no":
        break
    else:
        menu_list.append(menu)
    print(f"Your menu items is: {menu_list}, if you no need more then type 'no'.")

'''

'''
#Sum Until User Enters 0 (Keep asking the user to enter numbers. Add them to a total. Stop asking when the user enters 0, then print the total sum.)

user_input = 0

input_sum = []
num = ""

while num != user_input:
    num = int(input("Enter numbers that you have to sum: "))

    input_sum.append(num)
    print(f"the sum of your input numbers {input_sum} is: {sum(input_sum)}")

'''

'''
#ATM Simulation (Simulate a basic ATM. Show options like balance, deposit, withdraw, exit. Keep looping until the user chooses to exit.)

user_exit = "exit"

user_input = ""
bank_balance = 100000

while user_input != user_exit:
    user_input = str(input("What yoy have to do with your account: "))
    if user_input != user_exit:
        if user_input == "balance":
            print(f'Your bank balance is {bank_balance}')
        elif user_input == "d":
            print(f"How much you have to deposit: ")
            amount = int(input("Enter Amount: "))
            bank_balance += amount
            print(f"Clr Balance is {bank_balance}")
        elif user_input == "w":
            print(f"How much you have to withdraw: ")
            amount = int(input("Enter Amount: "))
            if amount <= bank_balance:
                bank_balance -= amount
                print(f"Clr Balance is {bank_balance}")
            else:
                print("insufficient fund")
    else:
        print("thank you")
        break

'''

'''
#Guess the Number (Generate a random number. Keep asking the user to guess until they get it right. Tell them when they’re correct.)

import random

guess_number = random.randint(1,100)
# print(f"The Random Number is: {guess_number}")

user_input = ""

while user_input != guess_number:
    user_input = int(input("Guess a number between 1-100: "))
    if user_input <= 100:
        if user_input > guess_number:
            print("Your guessing number is big")
        elif user_input < guess_number:
            print("Your gussing number is small")
        else:
            print("Successfully pick the wright number")
            break
    else:
        print("please enter a valid number")
        continue

'''

'''
#Input Validation (Only Numbers) (Ask the user for a number. If they enter letters or anything else, reject it and keep asking until they give a valid number.)

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        break
    print("Not a valid number. Try again.")
print("Thanks!")

'''

'''
#Find Factors of a Number (Ask the user for a number. Use a while loop to print all its factors (numbers that divide it evenly).)

i = 0
num = int(input("Enter a number which you have to find of it's factor under 0-100: "))
while (i <= 100):
    # print(i)
    i += 1

    if i%num == 0:
        print(i)

'''

'''
#Track Workout Reps (Ask the user how many reps they did each time. Keep adding to a total until the user types "done". Show the total reps at the end.)

total_reps = []

user_input = ""
total = 0

while user_input != "done":
    user_input = input("Enter your reps: ")
    if user_input !="done":
        total_reps.append(user_input)
    else:
        print("Thank you")
        for i in total_reps:
            total += int(i)
        print(f"Your Total reps os {total_reps} = {total}")

'''

'''
#Temperature Converter (Loop Until Exit) (Keep converting Celsius to Fahrenheit until the user types ‘q’ or ‘quit’. Use a while loop to keep the process going)

user_input = ""

while user_input != "q":
    user_input = input("convert 1. °C to °F or 2. °F to °C: ")
    if user_input == str(1):
        C = int(input("Enter °C temperature: "))
        print(f"°C to °F temperature is {(C* 9/5)+32}")
    elif user_input == str(2):
        C = int(input("Enter °F temperature: "))
        print(f"°F to °C temperature is {(C - 32)*5/9}")
    else:
        print("Thank You")
        break

'''

'''
#Typing Speed Test (Simplified)

import time

while True:
    input("enter any key to start: ")

    start = time.time()
    text = input("Enter a text and show your typing speed: ")
    end = time.time()

    print(f"You have taken {round(end - start, 2)} sec")

    if input("Try again y/n: ") != "y":
        break

'''

'''
#Car Start/Stop Engine Simulation (Simulate a car with commands like start, stop, quit. Use a while loop to process commands. Avoid repeating actions (e.g., starting when already started).)

started = False

while True:
    command = input("> ").lower()

    if command == "start":
        if started:
            print("car already started")
        else:
            print("car started")
            started = True
    elif command == "go":
        if not started:
            print("First You have to start the car")
        else:
            print("Go........")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            print("car stopped")
            started = False
    elif command == "quit":
        print("Game Over")
        break
    else:
        print("Please enter a valid command")

'''

#

with open("sample.txt", "r") as file:
    line = file.readline()

    while line:
        if "STOP" in line:
            print("STOP found")
            break
        print(line.strip())
        line = file.readline()


























