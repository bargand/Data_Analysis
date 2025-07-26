import numpy as np

'''
@ To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

@ The frompyfunc() method takes the following arguments:
@ function - the name of the function.
@ inputs - the number of input arguments (arrays).
@ outputs - the number of output arrays.
'''

def myaddition(x , y):
    return x+y

myadd = np.frompyfunc(myaddition, 2 , 1)

print(myadd([[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15], [16,17,18,19,20]]))


a = [[1,2,3,4,5], [6,7,8,9,10]]
b = [[11,12,13,14,15], [16,17,18,19,20]]

c = np.add(a ,b)
print(c)

#check the types of function
print(type(myaddition))
print(type(myadd))


# if np.add == np.ufunc:
#     print("add is ufunc")
# else:
#     print("add is not ufunc")