import numpy as np

arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([6,7,8,9,10])

arr_3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_4 = np.array([[[9,10],[11,12]],[[13,14],[15,16]]])

'''
#join the array with concatination() function

new_arr = np.concatenate((arr_1, arr_2)) #this function is just concat 2 array
print(new_arr)
'''

'''
#join the array with concatination() and axis


new_arr = np.concatenate((arr_3, arr_4),axis=2)
print(new_arr)
'''

'''
# concat with stack()

new_arr = np.stack((arr_1, arr_2))
new_array = np.stack((arr_3, arr_4))
print(new_arr)
print(new_array)
'''

'''
#concat with hstack()

new_arr = np.hstack((arr_1, arr_2)) #concat along rows
new_array = np.array((arr_3, arr_4))

print(new_arr)
print(new_array)
'''

'''
#concat with vstack()

new_arr = np.vstack((arr_1, arr_2)) # concat along coloum
new_array = np.vstack((arr_3, arr_4)) # concat along coloum

print(new_arr)
print(new_array)
'''

#concat with dstack()

new_arr = np.dstack((arr_1, arr_2)) # concat along height
new_array = np.dstack((arr_3, arr_4))

print(new_arr)
print(new_array)