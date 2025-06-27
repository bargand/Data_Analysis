'''
name = "debargha"

for name in name:
    print(name)

#or

name2= "tubai"

for i in name2:
    print(i)


name3 = ["tubai", "riya", "shruti", "debargha"]

for i in name3:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)


name3 = ["tubai", "riya", "shruti", "debargha"]

for i in name3:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)


for i in range(5):
    print(i)

#if i print 1 to 5 then i do

for j in range(5):
    print(j+1)

#or i can write like this

for k in range(0,5):
    print(k+1)
'''


arr = [503, 777, 324, 811, 861, 366, 470, 836, 964, 931, 367, 80, 520, 293, 176, 459, 215, 978, 756, 931]

print(len(arr))

for j in arr:
    print(j)
    if (j < 90):
        print("value is less than 80")
        break
    else:
        print("there is no value between 90")