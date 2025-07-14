# secrate code language generator

'''
import random
name = input("enter a name: ")

new_list1 = []
for i in range(3):
    ls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ran_ls = random.choice(ls)
    new_list1.append(ran_ls)
print(new_list1)

new_list2 = []
for i in range(3):
    ls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ran_ls = random.choice(ls)
    new_list2.append(ran_ls)
print(new_list2)



a = list(name[0])
b = list(name[1:])
c = new_list1+b+a+new_list2

sin_str = "".join(c)

print(sin_str)

'''

'''
import random

def my_fun(n=3, new_str=2):
    alpha = list("abcdefghijklmnopqrstuvwxyz")

    return [[random.choice(alpha) for _ in range(n)] for _ in range(new_str)]
new_str1,new_str2 = my_fun()

# print(new_str1)
# print(new_str2)

name = input("Enter the name: ")

a = list(name[0])
b = list(name[1:])
c = new_str1+b+a+new_str2

sin_str = "".join(c)

print(f"Your coded name is: {sin_str}")
'''

'''

name2 = sin_str

# x = list(name2[0:3])
# y = list(name2[-3:])

# print(x)
# print(y)

z = list(name2[-4])
# print(z)

i = list(name2[3:-4])
# print(i)

print(f"the decode name is: {"".join(z+i)}")

'''



import random

def my_fun(n=3, new_str=2):
    alpha = list("abcdefghijklmnopqrstuvwxyz")

    return [[random.choice(alpha) for _ in range(n)] for _ in range(new_str)]
new_str1,new_str2 = my_fun()

name = input("Enter the name: ")

a = list(name[0])
b = list(name[1:])
c = new_str1+b+a+new_str2

sin_str = "".join(c)

print(f"Your coded name is: {sin_str}")

name2 = sin_str

z = list(name2[-4])
i = list(name2[3:-4])

print(f"the decode name is: {"".join(z+i)}")