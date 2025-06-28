'''
#1. Print Numbers from 1 to 10

for i in range(0,10):
    print(i+1)
'''
'''

#2. Print Even Numbers from 1 to 20

for i in range(1,20,2):
    print(i+1)

'''
'''

#3. Calculate the Sum of All Numbers from 1 to 100

total = 0

for i in range(0, 100):
    total+=i+1

print("sum", total)


#or

total = 0

for i in range(0,101):
    total += i
print("sum", total)

'''

'''
#Print Each Character in a String

name = "Debargha"
for i in name:
    print(i)

'''

'''
#5. Count How Many Vowels Are in a String
string = "A Quick Brown Fox Jump Over The Leazy Dog"
vowels = "aeiouAEIOU"

count = 0

for i in string:
    if i in vowels:
        count += 1
print(count)

'''

'''
#6. Print a Right-Angled Triangle Using Stars
star = 50

for i in range(1,star+1):
    print("*"*i)

'''

'''
#print all number in a list
elm = [1,4,9,16,25,78,23,98,43,12,90]

for i in elm:
    print(i)

'''

'''
#Search a number

ser = [1,4,9,16,25,78,23,98,43,12,90]
searchElm = 25
index = 0

for i in ser:
    print(i)
    if (i==searchElm):
        print(searchElm,"is found and it is found in Index: ", index)
        break
    index += 1
'''

'''
#7. Loop Through a List and Print Only Numbers Greater Than 50

# for i in range(51,100):
#     print(i)

numList = [1,435,78,435,23,7,0,5,23,76,9,4,32,78,98,5,323,90]

for i in numList:
    if (i >= 50):
        print(i)

'''

'''
#8. Multiply All Elements in a List

numList = [1,435,78,435,23,7,5,23,76,9,4,32,78,98,5,323,90]
m = 1

for i in numList:
    m *= i
print(m)

'''
'''
#multiplication
numList = [1,435,78,435,23,7,5,23,76,9,4,32,78,98,5,323,90]
m =1

for i in numList:
    m*=i
print("Final result: ",m)
'''

'''
numList = [1,435,78,435,23,7,5,23,76,9,4,32,78,98,5,323,90]
m = 1
for i in numList:
    m -= i
print("Final result: ",m)

'''

'''
m = 1
for i in range(101):
    m += i
print(m)
'''

'''
#Average
m = 1
num= 100
for i in range(num):
    m += i/num
print(m)

'''

'''
#9. Reverse a String Using a Loop

"""
the different between revrse += i and the revrse = i+revrse is : this(revrse += i) is used for append and this (revrse = i+revrse) is used for prepand
"""

name = "debargha"
revrse = ""

for i in name:
    revrse = i + revrse
print(revrse)

'''

'''
#10. Print the Multiplication Table of a Number (e.g., 7)

num = int(input("Enter Your Number for Multiplication Table: "))

for i in range(1,11):
    print(f'{num} * {i} = {num*i}')

'''

'''
#Print All Prime Numbers Between 1 and 50
for i in range(2,51):
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if (i%j == 0):
            is_prime = False
            break
    if is_prime:
        print(i)
'''

'''
#Find the factorial of a number

num = int(input("Enter your number: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i
print(f'The factorial of {num}! is: {factorial}')

'''

'''
#Print numbers from 1 to 100, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz"

for i in range (1,101):
    if (i%15 == 0):
        print("it is multiples of 15: FizzBuzz")
    elif (i%5 == 0):
        print("it is multiples of 5: Buzz")
    elif (i%3 == 0):
        print("it is multiples of 3: Fizz")
    else:
        print(i)

'''

'''
#Find the sum of digits of a number (e.g., 1234 → 10)

num = int(input("Enter yoyr number that you have to sum: "))
summ = 0
for i in str(num):
    summ += int(i)
print(f"the sum of {num} is {summ}")

'''

#Remove duplicates from a list

primary_list = [1,2,2,3,3,3,4,5,6,7,7,6,4,3,2,5,7,8]
unique_list = []

for i in primary_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)


























































