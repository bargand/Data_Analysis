import numpy as np

'''
arr = np.array([1,2,3,4,5,6,7,8])

new_arr = arr.reshape(2,4)

# print(new_arr)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr2.reshape(4,3))


#convert 1D array to 3D array

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr2.reshape(4,1,3))

#unknown array convert

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr.reshape(3,3)) # here 3 is row and another 3 is colum
print(arr.reshape(3,3,1)) # here 3 is main array and another 3 is row and 1 is coloum


'''
#2D 3D array to 1D array

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12], [13,14,15,16]]])
print(f"This is {arr.ndim}D array")

new_arr = arr.reshape(-1) # it is defaultly change the _D array to 1 D
new_arr2 = arr.reshape(16) #the element is 16 and the if we will put it then it change into 1D array

print(f"The new array is{new_arr} and dimension is {new_arr.ndim}D")
print(f"The new array is{new_arr2} and dimension is {new_arr2.ndim}D")
