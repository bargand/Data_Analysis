'''
#Email Validator (Write a function is_valid_email(email) that returns True if the email is in a valid format (contains '@' and '.' after '@'), else False.)

def is_email_valid(email):
    if "@" in email and "." in email:
        print("True")
    else:
        print("False")

is_email_valid("debar@gmail.com")
is_email_valid("@.")
is_email_valid("debargha")

'''

'''
#BMI Calculator (Return BMI and a string indicating the health status (e.g., "Underweight", "Normal", "Overweight", "Obese").

def bmi(weight, height):
    cal = round((weight)/(height**2), 2)

    if cal < 16:
        print("Severe Thinness")
    elif 16 < cal < 17:
        print("Moderate Thinness")
    elif 17 < cal < 18.50:
        print("Mild Thinness")
    elif 18.50<cal<25:
        print("Normal")
    elif 25 < cal <30:
        print("Overweight")
    elif 30< cal < 35:
        print("Obese Class I")
    elif 35< cal < 40:
        print("Obese Class II")
    else:
        print("Obese Class III")
    print(f"your BMI is {cal} Kg/m^2")
bmi(90, 1.80)

'''

'''
#Password Strength Checker (Function: check_password_strength(password) (Return strength level: Weak, Medium, Strong (based on length, digits, special characters).

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
special_char = "!@#$%^&*()<>,.?/=+-_"

def check_pass(password):
    has_letter = any(char in string for char in password)
    has_number = any(char in num for char in password)
    has_special = any(char in special_char for char in password)

    if has_letter and has_number and has_special:
        print("Strong password")
    elif has_letter and has_number:
        print("Moderate strength password")
    else:
        print("Weak password")

check_pass("Tubai0012@*")  

'''

'''
#Tip Calculator (Function: calculate_tip(bill_amount, tip_percent) (Return total bill including tip.)

def bill(bill_amount, tip_percentage):
    percent = (bill_amount*tip_percentage)/100
    print(f"Your Total Bill amount is {round((bill_amount+percent) , 2)}")

bill(100,10)
bill(500,10)
bill(100,8)
bill(3982049,10)
bill(1324,7)

'''

'''
#Expense Tracker (Function: add_expense(expenses, category, amount) (Modify a dictionary to store categorized expenses.)

def add_expense(expense, category, price):
    if category in expense:
        expense[category] += price
    else:
        expense[category] = price
expense={
    "food": 30,
    "milk": 40
}

add_expense(expense, "food", 50)
add_expense(expense, "mango", 50)
add_expense(expense, "milk", 10)
add_expense(expense, "food", 50)

print(expense)

'''

#To-Do List Manager (Functions: add_task(todo_list, task), remove_task(todo_list, task), list_tasks(todo_list) (Build a command-line task manager with these functions.)

'''
toDo =["tubai"]

user_input = input("Do you want to 1. add(a) or 2. remove(r): ")

if user_input == "a":
    user_add_input = input("Add your todo: ")
    toDo.append(user_add_input)
    print(toDo)
elif user_input == "r":
    user_remove_input = input("remove your todo: ")
    toDo.remove(user_remove_input)
    print(toDo)
else:
    print("Please enter valid message")

'''

'''
#7: To-Do List Manager by implementing the three functions

def add_list(todo_list, task):
    if task not in todo_list:
        todo_list.append(task)
    else:
        print(f"{task} is already exist")

def remove_list(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
    else:
        print(f"{task} is not exist")

def list_task(todo_list):
    if not todo_list:
        print("The todo list is empty")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def run_to_manager():
    todo_list=[]

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Quit")

        user_input = input("Enter your command: ")

        if user_input == "1":
            task = input("Enter task to add: ")
            add_list(todo_list, task)
        elif user_input == "2":
            task = input("Enter task to remove: ")
            remove_list(todo_list, task)
        elif user_input == "3":
            list_task(todo_list)
        elif user_input == "4":
            print("thank you")
            break
        else:
            print("Invalid choice. Please try again.")

run_to_manager()

'''

'''
#URL Shortener (Mock) (Function: shorten_url(long_url) (Return a mock shortened version using hashing or a unique code.)


import pyshorteners

def shorten_url(long_url):

    if "https://" in long_url and "." in long_url:
        if len(long_url) > 28:
            s = pyshorteners.Shortener().tinyurl.short(long_url)
            lenght = len(long_url)
            print(s, lenght)
        else:
            print("Your url size is too small")
    else:
        print("Please enter a valid link")



shorten_url("https://pypi.org/project/pyshorteners/")
shorten_url("https://tinyurl.com/22l7bx24")
shorten_url("http:jkh.fkjdf")
shorten_url("https://www.google.com/search?q=url+short+pip&rlz=1C1ONGR_enIN1128IN1128&oq=url+short+pip&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQIxgnGIAEGIoFMgoIAhAAGLEDGIAEMg0IAxAAGIMBGLEDGIAEMg0IBBAAGIMBGLEDGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgYIBxAFGEDSAQgzMjgwajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
shorten_url(564)

'''

'''
#Text Summarizer (Function: summarize_text(text, max_sentences) (Return the first n sentences from the input.)

def summarize_text(text, max_sentences):
    sentences = text.split(" ")
    sen = sentences[0 : max_sentences]
    
    print(f"{" ".join(sen)}")

summarize_text("This is the first sentence. This is the second sentence. And this is the third.", 5)
summarize_text("This is the first sentence. This is the second sentence. And this is the third.", 3)
summarize_text("This is the first sentence. This is the second sentence. And this is the third.", 4)
summarize_text("This is the first sentence. This is the second sentence. And this is the third.", 10)

'''

'''
#Simple Weather Report Formatter (Function: format_weather_data(city, temperature, humidity) (Return a formatted weather summary string.)

def format_weather_data(city, temperature, humidity):
    return f"Weather forcast.\nIn {city} temperature is {temperature}°C and Humidity is {humidity}%"

report = format_weather_data("Kamarpukur", 32, 80)

print(report)

'''

'''
#Data Aggregator (CSV) (Function: summarize_csv(file_path) (Read a CSV file (e.g., sales.csv), return summary (e.g., total sales, average, by category).)

import csv

with open("vignaR.csv", "r") as file:
    render_file = csv.reader(file)

    for row in render_file:
        print(row)


import pandas as pd

df = pd.read_csv("SaleData.csv")

print(df.info())
        
'''

#User Authentication System Functions:(register_user(users, username, password) (authenticate_user(users, username, password) (Store users in a dictionary, password hashed (e.g., using hashlib).)

import hashlib

def register_user(users, username, password):
    """
    Register a new user with a username and hashed password.
    
    Args:
        users (dict): Dictionary of existing users
        username (str): New user's username
        password (str): New user's password
        
    Returns:
        dict: Updated users dictionary
    """
    if username in users:
        print("Username already exists. Please choose a different one.")
        return users
    
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Store the user information
    users[username] = {
        'password_hash': hashed_password
    }
    
    print(f"User '{username}' registered successfully.")
    return users

def authenticate_user(users, username, password):
    """
    Authenticate a user by verifying username and password.
    
    Args:
        users (dict): Dictionary of existing users
        username (str): User's username
        password (str): User's password
        
    Returns:
        bool: True if authentication succeeds, False otherwise
    """
    if username not in users:
        print("Authentication failed: Username not found.")
        return False
    
    # Hash the provided password to compare with stored hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if users[username]['password_hash'] == hashed_password:
        print(f"Authentication successful for user '{username}'.")
        return True
    else:
        print("Authentication failed: Incorrect password.")
        return False

# Example usage
if __name__ == "__main__":
    # Initialize an empty user dictionary
    users = {}
    
    # Register some users
    users = register_user(users, "alice", "securepassword123")
    users = register_user(users, "bob", "bobspassword")
    
    # Try to register an existing user
    users = register_user(users, "alice", "newpassword")
    
    # Test authentication
    authenticate_user(users, "alice", "securepassword123")  # Should succeed
    authenticate_user(users, "alice", "wrongpassword")      # Should fail
    authenticate_user(users, "charlie", "anypassword")      # Should fail (user doesn't exist)
















































