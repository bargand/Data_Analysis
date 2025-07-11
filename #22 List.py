'''
num = [1,2,3,4,5,6,7,8]

print(num)
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])
print(num[5])
print(num[6])

print(num[0:3])
print(num[0:3+1])

print(num[:6]) #if 6 then 6-1 is consider

print(num[2:]) # first argument is always in the proper place but in the secound argument it is in n-1

print(num[-1:-4])


print(len(num))

name = list(("debargha", "tubai", "riya", "prabir")) # this is the another way to print a list

print(type(name))

num[1:5] = [99,98,97,96,95]

## Insert in list
num.insert(1, "tubai") # first we use the order (where the we have to insert) second we use the argument what we have to insert 
num.insert(5, 900)
print(num)


#append

number = [12,45,67,12,67,23,78,45]

number.append(90) # in append we just add one argument

number.insert(3, 90) # in insert we just add an argument in a specific place


number2 = [90,45,87,95,35,15,48,68,35,17,84] # when we have more argument then we have to user extend
number.extend(number2)
print(number)

'''



#remove method in list

ani = ["lion", "monkey", "tiger", "fox"]

'''
#1st method for remove
ani.remove("tiger")

#2nd method
ani.clear()

#3rd method

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".

#4th method

ani.pop(1) # this will remove the specific item
ani.pop() # this will remove the last item is the list
print(ani)


#loops in list

thislist = ["apple", "banana", "cherry"]

for i in thislist:
    print(i)

# or

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

[print(i) for i in thislist]

'''

num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = []

for i in num1:
    num2.append(i)
    print(num2)
print(f"the numbers is{num2}")














