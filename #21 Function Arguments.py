'''
# There are 4 types of function arguments

1. Default arguments.
2. Keyword arguments.
3. variable length arguments.
4. Recuired arguments
'''

'''
# 1. Default arguments

def sum(a=4, b=4): # the a=4 and b=4 is a default value is in the function calling action i do not put the arguments then this default value are printed
    print(f"the average of a and b is: {(a+b)/2}")
sum(9, 1)
#or
sum(5) #if i want to put a value and want to leave the b value
#or
sum(b=7) #if is want to give the b value

'''

'''
# 2. required arguments

def sum(a , b=4):
    print(f"the average of a and b is: {(a+b)/2}")
sum(4,4)
#or
sum(a=3)

'''

'''
#keyword arguments

def name(fname, mname, lname):
    print(f"your name is {fname} {mname} {lname}")
name("prabir", "kumar", "nandi") # this is the normal way , in this case we have to aware about the order

name(fname="Prabir", lname="nandi", mname="kumar") # no eed to knowing the order

'''

'''
#3. variable length arguments.

def average(*numbers):
    print(f"the average of all numbers is: {sum(numbers)/2}")
average(2,2,2)

'''
# or another way to do this

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(f"the average of all numbers is {sum/len(numbers)}")
average(2,2,2)






