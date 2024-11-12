import random

#ROCK PAPER SCISSORS

rock = """
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


while True:
    user_choice = int (input("Enter an option : 0 for Rock, 1 for Paper, 2 for Scissors.\n "))
    gestures = [rock,paper,scissors]
    computer_choice = random.randint(0,2)
    options = ["Rock", "Paper","Scissors"]

    if user_choice > 2:
        print("Option is invalid,You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print(f"user: {gestures[user_choice]}\ncomputer: {gestures[computer_choice]}")
        print(f"{options[user_choice]} beats {options[computer_choice]}, You win!")
    elif user_choice ==2 and computer_choice == 0:
        print(f"user: {gestures[user_choice]}\ncomputer: {gestures[computer_choice]}")
        print("Rock beats scissors, You lose!")
    elif user_choice > computer_choice:
        print(f"user: {gestures[user_choice]}\ncomputer: {gestures[computer_choice]}")
        print(f"{options[user_choice]} beats {options[computer_choice]}, You win!")
    elif user_choice < computer_choice:
        print(f"user: {gestures[user_choice]}\ncomputer: {gestures[computer_choice]}")
        print(f"{options[computer_choice]} beats {options[user_choice]}, You lose!")
    else:
        print(f"user: {gestures[user_choice]}\ncomputer: {gestures[computer_choice]}")
        print("draw!")