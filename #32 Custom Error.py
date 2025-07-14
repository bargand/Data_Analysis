a = input("Enter message: ")

if (str(a) == "quit"):
    print("All work is done")
elif (5<=int(a)<=9):
    print("Good to go")
elif (int(a)<5 or int(a)>9):
    raise ValueError("value error")