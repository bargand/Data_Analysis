#Rock Paper Seaser game

import random

i = 0
total_point = 0
win_point = 1

while i<=9:
    i += 1


    random_number = random.randint(0,2)
    game_char = ["R" , "P" , "S"]
    random_game_char = game_char[random_number]

    user_input = input("Enter Your Choice(R/P/S): ")

    if random_game_char == user_input:
        print(f"Game Tie because you choose: {user_input}, Bot Choose: {random_game_char}")
    elif random_game_char == "R" and user_input == "P":
        print(f"You Win because you choose: {user_input}, Bot Choose: {random_game_char}")
        total_point += win_point 
    elif random_game_char == "R" and user_input == "S":
        print(f"Bot Win because you choose: {user_input}, Bot Choose: {random_game_char}")
    elif random_game_char == "P" and user_input == "R":
        print(f"Bot Win because you choose: {user_input}, Bot Choose: {random_game_char}")
    elif random_game_char == "P" and user_input == "S":
        print(f"You win because you choose: {user_input}, Bot Choose: {random_game_char}")
        total_point += win_point
    elif random_game_char == "S" and user_input == "R":
        print(f"You win because you choose: {user_input}, Bot Choose: {random_game_char}")
        total_point += win_point
    elif random_game_char == "S" and user_input == "P":
        print(f"Bot win because you choose: {user_input}, Bot Choose: {random_game_char}")
    else:
        print("I do not understand the prompt")

print(f"Your winning point is: {total_point}")