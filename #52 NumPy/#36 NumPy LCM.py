import numpy as np

'''
a = 4
b = 6

#The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
lm = np.lcm(a,b)
print(lm)

'''
#when our data is an array then we use reduce function with lcm function
lm_arr = np.array([1,5,9,3,2])

print(np.lcm.reduce(lm_arr))

lm_arran = np.arange(1,11)
print(np.lcm.reduce(lm_arran))