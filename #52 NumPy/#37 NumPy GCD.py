import numpy as np

'''
a = 6
b = 9

#The GCD (Greatest Common Devisor), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.

print(np.gcd(a,b)) 
'''

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

print(np.gcd.reduce(arr1, arr2))


