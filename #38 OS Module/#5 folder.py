import os
'''

folder = os.listdir("#38 OS Module/Data")

# print(folder)

for i in folder:
    print(i)


for i in folder:
    print(i)
    print(os.listdir(f"#38 OS Module/Data/{i}"))


file_to_run = "main.md"

os.system(file_to_run)
'''

#use to know the current directory

current_dir = os.getcwd()

#now we chnage the directory and priny the current directory and then its directory os changed

go_dir = os.chdir("#38 OS Module/Data")
current_dir = os.getcwd()

print(current_dir)