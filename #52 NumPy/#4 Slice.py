import numpy as np

'''
#one dim slicing

arr = np.array([1,2,3,4,5])

print(arr[0:4]) #1,2,3,4
print(arr[0:]) #1,2,3,4,5
print(arr[:5]) #1,2,3,4,5
print(arr[0:5:2]) #1,3,5

'''

#2wo dimension slicing

arr = np.array([[1,2,3,4],[5,6,7,8]])

print(arr[1, 0:3]) #5,6,7 
'''
This means in 1 index array and then you slice the components in 2nd array
'''
print(arr[0, -2:]) #3,4

print(arr[0:2, 2])  #3,7
'''
This means in 0 or 1st array and 2 or 2nd array just slice the 2nd index eliment
'''

print(arr[0:2, 1:3]) #2,3,6,7
'''
This means in 0 or 1st array and 2 or 2nd array just slice the 2nd index eliment
'''