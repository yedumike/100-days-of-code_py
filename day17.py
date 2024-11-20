from random import randint

#Number guessing game

EASY_LEVEL_TURNS =  10
HARD_LEVEL_TURNS = 5

"Number guessing game"

# Function to check user's guess against actual number
def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! Answer is {actual_answer}")




# Choose a random number from 1 to 100
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)

    # Function to set difficulty level
    def set_difficulty():
        level = input("What level?: type 'easy' or 'hard':\n")
        if level == 'easy':
            return EASY_LEVEL_TURNS
        else:
            level == 'hard'
            return HARD_LEVEL_TURNS


    # Let the user guess a number
    turns = set_difficulty()

    guess = 0
    while guess != answer and turns != 0:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You don't have remaining attempts")
    # Track the number of turns and reduce by 1 if they get it wrong
    # Repeat the guessing functionality if they get it wrong

game()