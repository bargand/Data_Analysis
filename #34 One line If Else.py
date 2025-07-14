a = 400
b = 50

if (a > b):
    print(f"{a} is greater than {b}")
elif (a == b):
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is less than {b}")
    

#instred of this we can write


print(f"{a} is greater than {b}") if (a > b) else print(f"{a} is equal to {b}") if (a == b) else print(f"{a} is less than {b}")