from numpy import random as rn

'''
#one random number under 0 to 100
x = rn.randint(100)
print(x)
'''
'''
#random float number generate between 0 and 1
x = rn.rand()
print(x)
'''
'''
#1D random array under 0 to 100
x = rn.randint(100, size=(5)) 
print(x)
'''
'''
#2D array generate

x = rn.randint(100, size=(3,5)) # 3 is row and 5 is coloum
print(x)

'''
'''
#3D array generate
x = rn.randint(100, size=(3,4,5)) #3 main array, 4 row and 5 coloum
print(x)
'''
'''
#similarly we can do this with float

x = rn.rand(5)
print(x)
'''
'''
#here we can not specify in which number you have to generate random number, here we just mention the row and coloum an dthe main array(dimension) that we have to create
x = rn.rand(5,3) #5 row and 3 coloum
print(x)
'''
'''
x = rn.rand(3,4,5) #3 main array, 4 row and 5 coloum
print(x)
'''
