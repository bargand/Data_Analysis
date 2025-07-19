'''
1. Dog Class
Question: Create a class Dog with a name attribute and a method bark() that prints "Woof!".

Description: Learn how to define a class, create an instance, use the __init__ method, and call an instance method.
'''
'''
class dog():
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(f"{self.name} is barking woof!!")
Dog = dog("Tommi")
Dog.bark()
'''

'''
2. Rectangle Area Calculator
Question: Create a Rectangle class with attributes width and height. Add methods area() and perimeter().

Description: Practice using attributes and performing operations inside class methods.
'''
'''
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        print(f"The rectangle area is: {(self.width)*(self.height)}")
    def perimeter(self):
        print(f"The perimeter is: {2*(self.height+self.width)}")

rect = Rectangle(20,10)
rect.area()
rect.perimeter()
'''

'''
3. Bank Account
Question: Create a BankAccount class with owner and balance. Add methods deposit(), withdraw(), and display_balance().

Description: Understand how to modify an object's state and enforce conditions (e.g., prevent withdrawing more than balance).
'''
'''
class BankAccount():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be possitive")
            return
        self.balance += amount
        print(f"Your deposit amount is: {amount} and clr balance is: {self.balance}")
    def withdraw(self, amount):
        if amount <= 0:
            print("withdraw amount must be positive")
            return
        self.balance -= amount
        print(f"Your withdraw amount is: {amount} and the clear balance is: {self.balance}")
    def total_balance(self):
        print(f"Your total balance is: {self.balance}")

Account = BankAccount("Debargha", 100)

Account.deposit(50)
Account.deposit(-50)
Account.withdraw(100)
Account.total_balance()

'''

'''
4. Student Grade Tracker
Question: Create a Student class with name, and a list of grades. Add a method average_grade().

Description: Practice managing internal data (lists) and computing derived values.
'''




















































































