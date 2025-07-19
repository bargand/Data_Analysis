user_name = input("Enter your name: ")
user_occupation = input("Enter your occupation: ")

class Person():
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
    def info(self):
        print(f"Name: {self.name}\nOccupation: {self.occupation}")

a = Person(user_name , user_occupation)

a.info()