'''
name1 = {"Aman Kumar", "Anargha Gopan", "Ankit Kumar", "Christina Mushahary", "Ganesula Jaya Veerendra", "Kriti Gupta", "Kummara Vardhan"}
name2 = {"Manisha Kumari", "Mehjabeen Rahman", "Prashanti Maiti", "Praveen Kumar Roy", "Rashtrapal Maroti Sonkamble", "Romit Roy"}
name3 = ["debargha", "nandi","tubai","abal"]

#update or add set
name1.add("debargha nandi")
# print(name1)

name1.update(name2)
print(name1)

name1.update(name3)
print(name1)

#clear set
name1.remove("Aman Kumar")
print(name1)


name1.discard("Aman Kumar")
print(name1)

name1.clear()
print(name1)


del name1
print(name1) # it returen error because the name 1 is deleted

name1.pop()
print(name1)


#loops in set
num1 = [12, 13, 13, 10, 13, 15, 7, 11, 14, 11, 11, 13, 15, 13, 14, 19, 13, 6, 23, 15, 17, 16, 11, 14, 15, 22, 18, 14, 11, 16, 17, 11, 12, 13, 10, 15, 14, 17, 12] 

num2 = [16, 27, 11, 27, 11, 15, 9, 16, 9, 13, 12, 21, 25, 15, 20, 18, 13, 13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21]

num3 = [13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21]

for i in num1:
    print(i)

'''

num1 = {1,2,3,4,5,6,6} 

num2 = {7,8,9,10,11,1,2}

num3 = {13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21}

'''
z = num1.union(num2) # it is add all numbers in a different sets
x = num1.intersection(num2) #if in set the item is samethen it output the same items
y = num1.difference(num2) #onno set a j gulo same segulo first seta bad die bakigulo show hobe
f = num1.difference_update(num2)
print(z)
print(x)
print(y)
print(f)

a = num1 | num2
print(a)

'''

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = {"a", "b", "c"}

g = x.issuperset(y)
h = y.issubset(z)


print(g)
print(h)




