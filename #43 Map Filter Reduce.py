#map
'''
def cube(x):
    return x**3
print(cube(2))

'''
'''

l = [1,2,3,4,5,6,7,8,9]
new_l = []

for i in l:
    new_l.append(i**3)
print(new_l)

# instrde of this we just built a cube function and do this
l = [1,2,3,4,5,6,7,8,9]

#cube function
cube = lambda x: x**3
# print(cube(2))

v_new_l = list(map(cube, l))
print(v_new_l)
'''

'''
#filter
l = [1,2,3,4,5,6,7,8,9,10]

def filter_func(x):
    return x >= 5

f_new_l = list(filter(filter_func , l))
print(f_new_l)
'''

#reduce

j = 0
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    j = j+i
print(j)

#instred of this we can dp this
l = [1,2,3,4,5,6,7,8,9,10]

from functools import reduce

sum_func = lambda x , y: x+y

r_new_l = reduce(sum_func , l)
print(r_new_l)