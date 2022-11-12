from random import random


user_input = input("Enter a choice : rock , paper , scissors")
Possibble_action = ["rock , paper , scissors"]
computer_action = random.choice(Possibble_action)

print(f"\nyou chose {user_input}, computer chose {computer_action}.\n")

if user_input == computer_action:
    print(f"Both players selected {user_input}. It's a tie!")

elif user_input == "rock":
    if computer_action == "scissors":
        print("rock smashes scissors! You win!")
    else:
        print("paper covers rock! You lose.")
elif user_input == "paper":
    if computer_action == "rock":
        print("paper covers rock! You win!")
    else:
        print("scissors cuts paper! You lose.")
elif user_input == "scissors":
    if computer_action == "paper":
        print("scissors cuts paper! You win!")
    else:
        print("rock smashes scissors! You lose.")                    
