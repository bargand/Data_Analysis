'''
f = open("myfile.txt" , "r")   #it give 2 arguments 1. name of the file and 2. mode(what you have to do) like (r)read, (w)write, (a)append etc

#read the file
text = f.read()
text2 = f.read(100)
print(text)
print(text2)

f.close()

'''

'''
#close file
f = open("myfile.txt" , "r")
print(f.read())

f.close()

'''

'''
#fileno

f = open("myfile.txt" , "r")
print(f.fileno())

'''

'''
#readable()
#The readable() method returns True if the file is readable, False if not.

f = open("myfile.txt", "r")

print(f.readable())

'''

'''
#append text

f = open("myfile.txt" , "a")

f.write("Debargha nandi")

f.close()

'''
'''
#instred of all this we can do this, in this method we habe no required for close the file

with open("myfile.txt" , "a") as f:
    f.write(" Hi i am a very bad boy")

'''

'''
#readline

f = open("myfile.txt" , "r")

i = 0

while True:
    line_read = f.readline()
    i += 1
    if not line_read:
        break
    else:
        m1 = int(line_read.split(",")[0])
        m2 = int(line_read.split(",")[1])
        m3 = int(line_read.split(",")[2])

        print(f"The math number of {i} is: {m1}")
        print(f"The math number of {i} is: {m2}")
        print(f"The math number of {i} is: {m3}")

'''

f = open("myfile.txt" ,"w")

line_write = [{32,78,90},{56,98,64},{98,25,84}]
for i in line_write:
    f.writelines(f"{i}\n")