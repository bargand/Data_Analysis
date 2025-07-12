questions = ["what is your name ?\n1. debar 2. tub 3. john", "what is your father name?\n1. debar 2. tub 3. john", "what is your first school\n1. debar 2. tub 3. john"]

total_amount = 0

for i in questions:
    print(i)
    if "what is your name ?\n1. debar 2. tub 3. john" in i:
        ans = input("ans >> ")
        if ans == "1":
            print("7 kadod")
            total_amount += 100
        else:
            print("futo sosti")
            total_amount -= 100
    elif "what is your father name?\n1. debar 2. tub 3. john" in i:
        ans = input("ans >> ")
        if ans == "2":
            print("7 kadod")
            total_amount += 100
        else:
            print("futo sosti")
            total_amount -= 100
    elif "what is your first school\n1. debar 2. tub 3. john" in i:
        ans = input("ans >> ")
        if ans == "3":
            print("7 kadod")
            total_amount += 100
        else:
            print("futo sosti")
            total_amount -= 100

if total_amount < 0:
    print("Taka die bari jabi, khelte aseche, dekhei bojha jacchilo khelte pare na")
else:
    print(f"you own: {total_amount}")
    
