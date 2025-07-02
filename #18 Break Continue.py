#Break when 10 is return and break the loops

for i in range(1,100):
    if i == 10:
        print("BREAK in", i)
        break
    else:
        print(i)


#continue : when is equal to 10 then only it break and then the rest of the logic work

for i in range(1,100):
    if i == 10:
        print("BREAK in", i)
        continue
    else:
        print(i)