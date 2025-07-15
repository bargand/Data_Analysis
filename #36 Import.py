'''

import math # if we import the full math function import

result = math.sqrt(2)
print(result)

result = math.pi
print(result)


from math import sqrt #if we import only one function in math


resu = sqrt(3) # then we not write math.sqrt instred of this we can write just sqrt()
print(resu)

# from math import *  #we can write this when we want to import all into the math function


#as syntax

import math as m

resul = m.pi
print(resul)


import math

print(dir(math))

'''

from deba import *

print(f"My name is {name} and my age is {age}")