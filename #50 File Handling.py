'''
We do Create, read update and delete

we use open() function to open the file.

There are different modes to open the file, and when we open it we have to be it close with close function(), but there was one method then can give use a features like if we open the file we have no need to close it.

MODES:

r - read
w - write
a - apppend
x - creat(if not exists)

we have to specrify that it is text or binary file

t - text
b - binary

rt - r for read and t for text
'''

#Here we need to close the open file
'''
f = open("myfile.txt", "r")
print(f.read())

f.close()


fg = open("deba.txt", "x")

fg.close()

'''

#but here we no need to close the open file

'''
with open("myfile.txt", "r") as f:
    print(f.read())

'''
'''
#we can specify which pare the code can read
with open("deba.txt", "r") as f:
    print(f.read(5))

'''

#readline() that will read the text in line by line
'''
with open("deba.txt", "rt") as f:
    print(f.readline()) # it will read only first line

    print(f.readlines()) # it will read all lines in the text file and return into a list or array

'''

#for loops in the read(). it will return all lines with for loops
'''
with open("deba.txt", "rt") as f:
    for i in f:
        print(i)

'''





#write methods

'''
#this append method will write lines without hamarage the existing lines in file, and if you exicute this code it will appending the lines all times after exicute the code
with open("deba.txt" , "a") as f:
    print(f.write("\nShruti\natri"))

with open("deba.txt" , "rt") as f:
    print(f.read())

'''
'''
#write mode

with open("myfile.txt" , "wt") as f:
    print(f.write("Debargha nandi is a good boy")) # exicuting this line there was print one number that is the length of the text

with open("myfile.txt", "rt") as f:
    print(f.read())
    for i in f:
        print(len(i))

'''





#delete file method
'''
1. file delete - remove()
2. folder delete - rmdir()
'''

'''
#file delete with remove function
import os

if os.path.exists("E:/Python New/good/good.txt"):
    os.remove("E:/Python New/good/good.txt")
else:
    print("file not exist")

'''

'''
#folder delete

import os

os.rmdir("E:/Python New/good")

'''


















































