import random

options = ["rock", "paper", "scissors"]
pc_score = 0
user_score = 0

while True:
    user_input = input("Rock, paper, scissors? Press Q to quit. \n").lower()
    if user_input == "q":
        question = input("Quit the game? Y/N \n").lower()
        if question == ("y").lower():
            break
        if question == ("n").lower():
            print("Alright, let's go!")
            continue

    if user_input not in options:
        print("Please, pick one of the options.")
        continue
    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissors :2
    pc_pick = options[random_number]
    print("The oponent chose " + pc_pick +".")

    if user_input == "rock" and pc_pick == "scissors":
        print("You win.")
        user_score += 1
    elif user_input == "scissors" and pc_pick == "paper":
        print("You win.")
        user_score += 1
    elif user_input == "rock" and pc_pick == "paper":
        print("The oponent wins.")
        pc_score += 1
    elif user_input == pc_pick:
        print("It's a tie!")
    else:
        print("You lose.")
        pc_score += 1

print("You won " + str(user_score) + " times.")
print("The oponent won " + str(pc_score) + " times.")
if user_score > pc_score:
    print("CG, YOU WIN!:)")
if pc_score > user_score:
    print("You lose. Try again :(")