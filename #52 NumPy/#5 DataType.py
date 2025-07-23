import numpy as np

arr = np.array([1,2,3,4,5])

#to find the deta type we just write this code

print(arr.dtype)

#if we just assign the value as a specific datatype then

arr2 = np.array([1.2,3.8,4.3,9.7], dtype='i') #here i means int, we just convert float to int datatype

print(arr2, arr2.dtype)

#there are not changable data type like str to int, if we try then terminal through an error
'''
arr3 = np.array(["A", "B", "C", "D", "E"], dtype="i")
print(arr3, arr3.dtype)
'''

arr4 = np.array([-1,0,1,2])
new_arr4 = arr4.astype(bool)
print(new_arr4)

#we can change one data type to nother data type in a new array like

old_arr = np.array([1.3,2.9,3.5,4.0,5.1])

new_arr = old_arr.astype(int)
#or
new_arr = old_arr.astype('i')
print(new_arr, new_arr.dtype)
