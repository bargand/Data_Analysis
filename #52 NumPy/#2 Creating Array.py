#create a simple array

import numpy as np

arr_0 = np.array(43)
arr_1 = np.array([1,2,3,4,5,6])
arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
arr_3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
arr_u = np.array([1,2,3,4], ndmin=5) # to create one dimension array to 5 dimension

print(f"The array is: {arr_0} and this is {arr_0.ndim} dimension")
print(f"The array is: {arr_1} and this is {arr_1.ndim} dimension")
print(f"The array is: {arr_2} and this is {arr_2.ndim} dimension")
print(f"The array is: {arr_3} and this is {arr_3.ndim} dimension")
print(f"The array is: {arr_u} and this is {arr_u.ndim} dimension")