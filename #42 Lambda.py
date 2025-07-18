def double(x):
    return x**2
print(double(5))


#this instred we just write (use when we want to pass function in an argument)

double = lambda x: x**2
cuber = lambda y: y**3

# lambda can take multipe arguments

avg = lambda x,y,z : (x+y+z)/3
print(double(5))
print(cuber(5))
print(round(avg(3,5,6),2))


def fut(fx , value):
    return 8 + (fx ** value)
print(fut(2 , 3))

#or

def fut(fx , value):
    return 8 + fx(value)
print(fut(cuber, 2)) #use function in function





