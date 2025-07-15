'''
x = 100

def my_func():
    x = 1
    print(x) #Output should be 1 because it is local variable
my_func()

print(x) # output should be 100 because it is a global variable
'''

"""

x = 100

def my_func():
    x = 1
    y = 2
    print(x)
    print(y)
    '''
    This 2 are local variable thats why it could print the x and y value in the terminal
    '''
my_func()

print(x)
'''
print(y) # this line is through error because y declare as a local variable in the function, and this local variable is destroy when the function is exicuted. thats why at the end y not have any value to show and it will trrough error.
'''

"""

#we can declate the local variable as a global variable just like this

x = 100

def my_func():
    global x , y # this line will transform the variable as a global variable
    x = 1
    y = 2
    print(f"This is local x value: {x}")
my_func()
print(f"This is global x value: {x}")
print(f"This is global y value: {y}")

