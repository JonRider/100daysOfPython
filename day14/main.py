from art import logo, vs
from game_data import data
import random
from os import system


def print_vs(A, B):
    """Formats and prints A vs B"""
    print(
        f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(
        f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")


def compare_followers(A, B):
    """Compare number of social media followes. Returns 'a' or 'b'"""
    if A['follower_count'] > B['follower_count']:
        return 'a'
    else:
        return 'b'


# Start Game
print(logo)
score = 0
A = random.choice(data)
right = True
while right:
    B = random.choice(data)
    while A == B:
        B = random.choice(data)
    print_vs(A, B)

    # Compare followers
    high = compare_followers(A, B)

    # Get Choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check answer
    if choice == high:
        score += 1
        system("clear")
        print(f"You're right! Current score: {score}")
        if high == 'b':
            A = B
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        right = False
