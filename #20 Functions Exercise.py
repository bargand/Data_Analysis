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

def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

# Initial expense record
expenses = {
    "food": 100,
    "transport": 50
}

# Add expense to an existing category
add_expense(expenses, "food", 25)

# Add expense to a new category
add_expense(expenses, "entertainment", 60)

# Final output
print(expenses)















































































