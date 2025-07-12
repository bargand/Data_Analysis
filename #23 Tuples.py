name = ("Aman Kumar", "Anargha Gopan", "Ankit Kumar", "Christina Mushahary", "Ganesula Jaya Veerendra", "Kriti Gupta", "Kummara Vardhan", "Manisha Kumari", "Mehjabeen Rahman", "Prashanti Maiti", "Praveen Kumar Roy", "Rashtrapal Maroti Sonkamble", "Romit Roy")

'''
print(type(name))
print(len(name))

print(name)

print(name[0])
print(name[2])
print(name[2:8])
print(name[-2])


y = list(name)
y[3] = "kjhfkjdjfdjgfjd"
print(y)

if "Christina Mushahary" in y:
    print("yes")
else:
    print("no")


y = list(name)
y.insert(1, "ffffffff")
print(y)



y = list(name)
y.append("debargha nandi")
print(y)


y = list(name)
y.remove("Aman Kumar")
print(y)

if "Aman Kumar" in y:
    print("yes")
else:
    print("no")


y = list(name)

del y
print(y) # this is through error because y is deleted


#unpacking the tuples
(yellow, green, *red) = name

print(yellow)
print(green)
print(red)


#loops in tuples

j = 1
for i in name:
    print(f"{j} {i}")
    j+=1


for i in range(len(name)):
    print(name[i])

i = 0
while i < len(name):
    print(name[i])
    i+=1


#join tuples

num1 = (12, 13, 13, 10, 13, 15, 7, 11, 14, 11, 11, 13, 15, 13, 14, 19, 13, 6, 23, 15, 17, 16, 11, 14, 15, 22, 18, 14, 11, 16, 17, 11, 12, 13, 10, 15, 14, 17, 12) 

num2 = (16, 27, 11, 27, 11, 15, 9, 16, 9, 13, 12, 21, 25, 15, 20, 18, 13, 13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21)

num3 = (13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21)


final_num = num1+num2+num3

print(final_num)


#count and index
num3 = (13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21)

print(num3.count(13))
print(num3.index(15))

'''












