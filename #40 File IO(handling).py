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

#readable()
#The readable() method returns True if the file is readable, False if not.

f = open("myfile.txt", "r")

print(f.readable())


