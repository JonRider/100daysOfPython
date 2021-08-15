# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def check_number(guess, number, number_of_guesses):
    """Take a number guess and check it against the answer"""
    if guess == number:
        print(f"You got it! The answer was {number}.")
    elif guess > number:
        print("Too high.\nGuess again.")
        return number_of_guesses - 1
    else:
        print("Too low.\nGuess again.")
        return number_of_guesses - 1

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_TURNS
    elif difficulty == 'hard':
        return HARD_TURNS


# Get random Number
def game():
    number = random.randint(1, 100)
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Psst... the correct answer is {number}")
    number_of_guesses = set_difficulty()

    # Let them guess
    guess = 0
    while guess != number:
        if number_of_guesses > 0:
            print(f"You have {number_of_guesses} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            number_of_guesses = check_number(guess, number, number_of_guesses)
        else:
            print("You've run out of guesses, you lose.")
            return

# Start the Game
game()
