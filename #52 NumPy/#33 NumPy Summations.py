import numpy as np

# Summations is evaluate with two function add() and sum()

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

a = np.add(arr1, arr2) #it will add the elements with hight wise
print(a)

'''
b = np.sum([arr1, arr2]) #it will add the all elements in a single int
print(b)

c = np.sum([arr1, arr2], axis=1) #it will add elements width wise and give output in a single array
print(c)

d = np.cumsum(arr1) # it will add one by one with firts element like: E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
print(d)

'''