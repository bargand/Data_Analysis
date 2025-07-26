import numpy as np

'''
There are some rounding decimel functions like

1. truncation: Remove the decimals, and return the float number closest to zero.
2. fix: Remove the decimals, and return the float number closest to zero.
3. rounding : round off to 1 decimal point, 3.16666 is 3.2
4. floor: The floor() function rounds off decimal to nearest lower integer.(E.g. floor of 3.166 is 3.)
5. ceil: The ceil() function rounds off decimal to nearest upper integer. (E.g. ceil of 3.166 is 4.)
'''

a = np.array([-9.56789, -6.8234, 3.9345678, 1.82345])

b = np.trunc(a) # just removing the decimel part
c = np.fix(a) #similar as trunc

d= np.around(a, 2) # just given the 2 decimel point like this code, if here is 3 is present then it gives 3 decilem points

e = np.floor(a) #newrest lower int

f = np.ceil(a) #nearest higher int

print(b)
print(c)
print(d)
print(e)
print(f)