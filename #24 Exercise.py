#koun banega kadodpati game

questions = ["what is your name ?\n1. debar 2. tub 3. john", "what is your father name?\n1. debar 2. tub 3. john", "what is your first school\n1. debar 2. tub 3. john"]

total_amount = 0

for i in questions:
    print(i)
    ans = int(input("ans >> "))
    if 1 <= ans <= 3:
        if "what is your name ?\n1. debar 2. tub 3. john" in i:
            if ans == 1:
                print("7 kadod")
                total_amount += 100
            else:
                print("futo sosti")
                total_amount -= 100
        elif "what is your father name?\n1. debar 2. tub 3. john" in i:
            if ans == 2:
                print("7 kadod")
                total_amount += 100
            else:
                print("futo sosti")
                total_amount -= 100
        elif "what is your first school\n1. debar 2. tub 3. john" in i:
            if ans == 3:
                print("7 kadod")
                total_amount += 100
            else:
                print("futo sosti")
                total_amount -= 100
    else:
        print("please enter a valid choice")
        break

if total_amount < 0:
    print("Taka die bari jabi, khelte aseche, dekhei bojha jacchilo khelte pare na")
else:
    print(f"you own: {total_amount}")
    




########################################
########################################
########################################
#########another way to solve this problem#########
########################################
########################################

questions = [
    "What is the capital of India?\n1. Mumbai 2. Delhi 3. Kolkata",  # Answer: 2
    "Which planet is known as the Red Planet?\n1. Earth 2. Mars 3. Jupiter",  # Answer: 2
    "What is the national bird of India?\n1. Peacock 2. Parrot 3. Eagle",  # Answer: 1
    "Who wrote the Ramayana?\n1. Kalidas 2. Valmiki 3. Tulsidas",  # Answer: 2
    "Which is the largest mammal?\n1. Elephant 2. Blue Whale 3. Giraffe",  # Answer: 2
    "What is H2O commonly known as?\n1. Salt 2. Water 3. Oxygen",  # Answer: 2
    "Which festival is known as the festival of lights?\n1. Holi 2. Eid 3. Diwali",  # Answer: 3
    "Who is known as the Father of the Nation in India?\n1. Subhash Chandra Bose 2. Mahatma Gandhi 3. Jawaharlal Nehru",  # Answer: 2
    "Which sport is Sachin Tendulkar associated with?\n1. Football 2. Tennis 3. Cricket",  # Answer: 3
    "What is the currency of Japan?\n1. Dollar 2. Yen 3. Won"  # Answer: 2
]

answers = [2, 2, 1, 2, 2, 2, 3, 2, 3, 2]


total_amount = 0

for q, correct_ans in zip(questions, answers):
    print(q)

    try:
        ans = int(input("ans >> "))
        if 1 <= ans <= 3:
            if ans == correct_ans:
                print("7 kados")
                total_amount += 100
            else:
                print("futo sosti")
                total_amount -= 100
        else:
            print("Please enter a valid choice")
    except:
        print("please enter the choice value with 1-3")

if total_amount < 0:
    print("Taka die bari jabi, khelte aseche, dekhei bojha jacchilo khelte pare na")
else:
    print(f"you own: {total_amount}")
