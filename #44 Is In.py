'''
a = 4
b = "4"

print(a == b) # value
print(a is b) #exact locatin in object in memory



# if the variable is mutable then python store the data as a changable then "is" return false but if the variavle data is immutable then python store the data as a not changable part and then "is" return True

x = [1,2,3,4,5]
y = [1,2,3,4,5]

print(x == y)
print(x is y) # it returns false because the list is mutable

c = (1,2,3,4,5)
d = (1,2,3,4,5)

print(c == d)
print(c is d) # it returns true because tuples is immutable

'''

i = {"r":56, "u":78, "k":90}
j = {"r":56, "u":78, "k":90}

print(i == j)
print(i is j)