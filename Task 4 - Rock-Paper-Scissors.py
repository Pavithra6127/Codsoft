
# Task-4-Rock-Paper-Scissors Game

import random

print("Welcome to Rock-Paper-Scissors!")

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    elif user in ["rock", "paper", "scissors"]:
        print("You lose!")
    else:
        print("Invalid input!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye!")
        break
