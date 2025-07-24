from numpy import random 

#here choice means under this 4 choice the new array is created, "p" means probablity and under probablity we can told the array that the a number can how much percentage to generate(0.1 means 10%, and 0.0 means 0%) and the last size means 50 eliment array is created after exicuted
'''
print(random.choice([2,5,8,9], p=[0.1, 0.3, 0.6, 0.0], size=50)) 
'''
'''
#creating 2D array
print(random.choice([4,8,9,2], p=[0.1, 0.3, 0.6, 0.0], size=(5,3))) # in size 5 row and 3 is coloum

'''
#3D array created
print(random.choice([4,8,9,2], p=[0.1, 0.3, 0.6, 0.0], size=(3,5,3))) # in size 3 main array , 5 row and 3 is coloum