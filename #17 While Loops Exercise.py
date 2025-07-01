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






