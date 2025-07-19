'''
class person:
    name = "Debargha"
    occupation = "Web Dev"
    age = 23
    education = "Agriculture"

    def info(self):
        print(f"{self.name} is {self.age} years old")



a = person()

print(a.name)
print(a.age)
a.info() #i will call the function in the class

'''

'''
class person():
    name = " "
    age = 0

    def info(self):
        print(f"name: {self.name}\nAge: {self.age}")

a = person()

a.name = "Debargha"
a.age = 23

a.info()

'''

'''
'''
class person():
    name = ""
    age = 0

    def __str__(self):
        return(f"Name: {self.name}\nAge: {self.age}")

user_input_name = str(input("Enter prompt: "))
user_input_age = int(input("Enter age; "))

user_input_name = person()

user_input_name.name = user_input_name
user_input_name.age = user_input_age



'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = person("Debargha" , 23)

print(p.name)
print(p.age)

'''





















































