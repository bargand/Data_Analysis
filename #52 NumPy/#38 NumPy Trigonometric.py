import numpy as np

'''
x = np.sin(np.pi/2)
print(x)

y = np.array([np.pi/2, np.pi, np.pi/3, np.pi/4])

print(np.sin(y))
'''
'''
#Convert Degrees Into Radians

a = np.array([0, 90, 180, 360])
print(np.deg2rad(a))

#Radians to Degrees

b1 = np.array([1,2,3,4,5,6])
b2 = np.array([0, 1.57079633, 3.14159265, 6.28318531])

print(np.rad2deg(b1))
print(np.rad2deg(b2))
'''
'''
x = np.arcsin(1)
print(x)

y = np.array([1, 9.787, 1.57, 4.899])
print(np.arcsin(y))
print(np.arccos(y))
print(np.arctan(y))

'''

#convert 50 deg into redian

print(np.deg2rad(50))