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
#replace
ani = ["lion", "monkey", "tiger", "fox"]
ani[2] = "Debargha"
print(ani)




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


num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = []

for i in num1:
    num2.append(i)
    print(num2)
print(f"the numbers is{num2}")

'''

'''
#short list

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


name = ["Aman Kumar", "Anargha Gopan", "Ankit Kumar", "Christina Mushahary", "Ganesula Jaya Veerendra", "Kriti Gupta", "Kummara Vardhan", "Manisha Kumari", "Mehjabeen Rahman", "Prashanti Maiti", "Praveen Kumar Roy", "Rashtrapal Maroti Sonkamble", "Romit Roy", "Roshan Kumar Rai", "Saumyanetra Dattamajumder", "Shankhashubhra Sahoo", "Sivangee Dhar", "Sovan Lal Ghara", "Sumit Kumar", "Taushif Ahammed Molla", "Deepak Jangid", "Farhat", "Jyotinmoy Ghosh", "Kengam Mani Kumar", "Khushboo Solanki", "Kumari Shalini", "Lakshmigayatri Kolluri", "Manish Kumar Toppo", "Mayukh Nath", "Mohit Kumar Dubey", "Mona Kumari", "Mrinal Kumar", "Abinash Kabi", "Afifa Siddika", "Akansha Singh", "Anirban Samanta", "Anish R", "Arghanil Ghosh", "Arjya Kumar", "Ashok Saini", "Avik Pramanik", "Baishali Biswas", "Barsha Mishra", "Bhawani Kumari", "Nimish Mishra", "Pate Yakum", "Pratanu Sarkar", "Pritam Maity", "Pushpendra Singh", "Rachamallu Akhileswar Reddy", "Rahul Yadav", "Ritam Dutta", "Rohit Choudhary", "Rupam Das", "Rushita Anand", "Saloni Singh", "Saumadeep Chakraborty", "Sayan Mukherjee", "Shraddha Mohapatra", "Shubham Singh", "Simran Keshri", "Srinjoyee Ghorui", "Subhadeep Banerjee", "Subhadeep Karmakar", "Suman Samanta", "Swati", "Swati Priya", "Swetapadma Jena"]

for i in range(len(name)):
    name.sort()
    print(name[i])
    i += 1


num = [12, 13, 13, 10, 13, 15, 7, 11, 14, 11, 11, 13, 15, 13, 14, 19, 13, 6, 23, 15, 17, 16, 11, 14, 15, 22, 18, 14, 11, 16, 17, 11, 12, 13, 10, 15, 14, 17, 12, 16, 27, 11, 27, 11, 15, 9, 16, 9, 13, 12, 21, 25, 15, 20, 18, 13, 13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21]

num.sort()
print(num)

num.sort(reverse=True)
print(num)

'''

'''
#copy list

num = [12, 13, 13, 10, 13, 15, 7, 11, 14, 11, 11, 13, 15, 13, 14, 19, 13, 6, 23, 15, 17, 16, 11, 14, 15, 22, 18, 14, 11, 16, 17, 11, 12, 13, 10, 15, 14, 17, 12, 16, 27, 11, 27, 11, 15, 9, 16, 9, 13, 12, 21, 25, 15, 20, 18, 13, 13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21]

number = num.copy()

print(number)

num2 = list(number)
print(num2)

'''

'''
# add list

num1 = [12, 13, 13, 10, 13, 15, 7, 11, 14, 11, 11, 13, 15, 13, 14, 19, 13, 6, 23, 15, 17, 16, 11, 14, 15, 22, 18, 14, 11, 16, 17, 11, 12, 13, 10, 15, 14, 17, 12] 

num2 = [16, 27, 11, 27, 11, 15, 9, 16, 9, 13, 12, 21, 25, 15, 20, 18, 13, 13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21]

num3 = [13, 13, 15, 16, 18, 18, 13, 11, 5, 11, 15, 21]

name = ["Aman Kumar", "Anargha Gopan", "Ankit Kumar", "Christina Mushahary", "Ganesula Jaya Veerendra", "Kriti Gupta", "Kummara Vardhan", "Manisha Kumari", "Mehjabeen Rahman", "Prashanti Maiti", "Praveen Kumar Roy", "Rashtrapal Maroti Sonkamble", "Romit Roy"]

num3 = num1+num2+num3+name
print(num3)
count_number = num3.count(11)
count_name = num3.count("Anargha Gopan")
print(count_name)


for i in num2:
    num1.append(i)
# print(num1)

num1.extend(num2)
# print(num1)

'''

