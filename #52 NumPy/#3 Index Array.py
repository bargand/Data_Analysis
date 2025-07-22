import numpy as np

'''
#1 dimenson array indexing

arr = np.array([1,2,3,4,5])

print(arr[1]) # output 2
print(arr[0]) # output 1
print(arr[-1]) # output 5
'''

'''
#2 dim arr indexing

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[0,0]) # output 1
print(arr[0,-1]) # output 5
print(arr[0,2]) # output 3

print(arr[1,0]) # output 6
print(arr[1,-1]) # output 10
print(arr[1,3]) # output 9
'''

'''
#3 dim arr indexing

arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
arr_2 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

print(arr[0,2,2]) # if the 3 dimension array is look like 1 dimension then first 0 is just for showing.
print(arr_2[1,0,2]) # if it is looks like 3 dimension then first to last digit is workable.

print(arr_2[1,1,-1]) #output 16
print(arr_2[1,0,-1]) #output 12
'''

arr_u = [[[[[1,2,3,4,5]]]]]

print(arr_u[0]) #output 5