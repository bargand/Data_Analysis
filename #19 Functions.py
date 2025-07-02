'''

gmean1 = (a*b)/(a+b)

# print(gmean1)


gmean2 = (c*d)/(c+d)
# print(gmean2)

'''

'''
a = 8
b = 9

c = 5
d = 1

def geomean(a,b):
    gmean = (a*b)/(a+b)
    print(gmean)

    if (a>b):
        print(f"{a} is Greater than {b}")
    else:
        print(f"{b} is Greater than {a}")

geomean(a,b)
#or
geomean(6,9)
'''

def lessThan (x,y):
    pass


#simple name showing function

def name(Fname, Lname, age, gender):

    if gender == "male":
        print(f"hello {Fname} {Lname}, and his Age: {age}")
    if gender == "female":
        print(f"hello {Fname} {Lname}, and her Age: {age}")

name("debargha","nandi",23, "male")
name("Riya","nandi", 32, "female")
name("Supriya","nandi", 47, "female")
name("Prabir","nandi", 56, "male")
name("Rituraj","Pandit", 2, "male")




