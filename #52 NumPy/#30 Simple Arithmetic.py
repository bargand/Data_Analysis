import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

'''
#Addition
z = np.add(x,y)
print(z)

#substruction

z = np.subtract(x ,y)
print(z)

#multiplication

a = np.multiply(x ,y)
print(a)

#divided

b= np.divide(x ,y)
print(b)

#mod or reminder

c = np.mod(x,y)
d = np.remainder(x,y)
print(c, d)

#power

e = np.power(x,y)
print(e)


#Quotient and Mod(The divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.)

#first array will show the quotient and second array will show the mod or reminder

'''
f = np.divmod(x,y)
print(f)

#absolute value

g = np.array([-9,-6,7.9, -4.6]) 

h = np.abs(g) # remove the negetive symbole
print(h)