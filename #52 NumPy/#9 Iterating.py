import numpy as np

'''
# for 1D array iterating
arr = np.array([1,2,3,4,5,6,7,8])

for i in arr:
    print(i)

'''
'''
#2d arrat iterating

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

for i in arr:
    #print(i) # it just print the array not the element
    for j in i:
        print(j) #to print all elemts in array we do this

'''

#3d array iterating

arr = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12], [13,14,15,16]]])

for i in arr:
    # print(i)
    for j in i:
        # print(j)
        for k in j:
            print(k)

#upper portion is not recomended for the higher order dimension array iterating
#to do in a simple way we can do that

for i in np.nditer(arr):
    print(i)