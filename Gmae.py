# ROCK , PAPER , SCISSORS
import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice 'rock','paper','scissors',[quit , exist]  :")
    if user_choice == "quit":
        print("Thanks for playing")
        break

    elif user_choice not in choices:
        print("Wrong! TRY AGAIN")
        continue

    computer_choice = random.choice(choices)
    print(f"You won : {user_choice}")
    print(f"Computer won : {computer_choice}")

    if user_choice == computer_choice:
        print("Its a tie")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        print("You won")

    else:
        print("computer won")

print()
