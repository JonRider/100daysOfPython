from art import logo, vs
from game_data import data
import random
from os import system


def print_vs(A, B):
    """Formats and prints A vs B"""
    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def check_answer(a_followers, b_followers, choice):
    """Checks which answer is right and returns true if user is correct"""
    if a_followers > b_followers:
        return choice == 'a'
    else:
        return choice == 'b'


# Start Game
print(logo)
score = 0
A = random.choice(data)
is_right = True
while is_right:
    B = random.choice(data)
    while A == B:
        B = random.choice(data)

    # Print VS Text
    print_vs(A, B)

    # Get Choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Compare followers and check answer
    a_followers = A['follower_count']
    b_followers = B['follower_count']
    is_right = check_answer(a_followers, b_followers, choice)

    # Check answer
    if is_right:
        score += 1
        system("clear")
        print(logo)
        print(f"You're right! Current score: {score}")
        A = B
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
