#traditional method to sum two arrays
'''
x = [1,2,3,4]
y = [5,6,7,8]
z = []

for i , j in zip(x , y):
    z.append(i+j)
print(z)
'''

#usinf numpy we can add the array like this
import numpy as np
x = [1,2,3,4]
y = [5,6,7,8]

z = np.add(x,y)
print(z)


a = np.multiply(x,y)
print(a)

b = np.divide(x,y)
print(b)

c = np.subtract(x,y)
print(c)
