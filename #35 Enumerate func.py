'''
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(tuple(y))
'''

'''
index = 0
x = ('apple', 'banana', 'cherry')

for i in x:
    print(index, i)
    index += 1



#instred of this i could be do

x = ('apple', 'banana', 'cherry')

for index , i in enumerate(x):
    print(index, i)

'''
y = "debargha"

for index, i in enumerate(y):
    print(index+1, i)

#we can do this instred of

y = "debargha"

for index, i in enumerate(y, start=1):
    print(index, i)