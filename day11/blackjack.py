############### Blackjack Project #####################

#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random
from os import system

def deal(deck, hand, num):
    """Deal the requested number of cards to a hand"""
    for i in range(num):
        card = random.choice(deck)
        hand.append(card)
    return hand

def get_total(hand):
    """Get the total value of a hand"""
    total = sum(hand)

    if 11 in hand and total > 21:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    return total

def check_over(player_hand, computer_hand):
    player_total = get_total(player_hand)
    computer_total = get_total(computer_hand)
    if player_total > 21:
        return "You went over. You lose =("
    elif computer_total > 21:
        return "Opponent went over. You win ;)"
    else:
        return False

def check_win(player_hand, computer_hand):
    if get_total(player_hand) == get_total(computer_hand):
        return "Draw :|"
    elif get_total(player_hand) == 21 and len(player_hand) == 2:
        return "Blackjack! You win! =)"
    elif get_total(computer_hand) == 21 and len(computer_hand) == 2:
        return "Lose, opponent has Blackjack :o"
    elif get_total(player_hand) > get_total(computer_hand):
        return "You win :)"
    else:
        return "You lose :("

def final(player_hand, computer_hand):
    print(f"    Your final hand: {player_hand}, final score: {get_total(player_hand)}")
    print(f"    Computers final hand: {computer_hand}, final score: {get_total(computer_hand)}")

def play():
    print(logo)
    # Deck of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    computer_hand = []

    # Get starting Cards
    player_hand = deal(cards, player_hand, 2)
    computer_hand = deal(cards, computer_hand, 2)

    # Keep dealing
    dealing = True
    while dealing:
        score = get_total(player_hand)
        computer_score = get_total(computer_hand)
        print(f"    Your cards: {player_hand}, current score: {score}")
        print(f"    Computers first card: {computer_hand[0]}")
        # Check for bust
        is_over = check_over(player_hand, computer_hand)
        if not is_over:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
                dealing = False
                print(check_win(player_hand, computer_hand))
            else:
                # Deal another card
                player_hand = deal(cards, player_hand, 1)
        else:
            print(is_over)
            dealing = False

        # See if computer should draw
        while computer_score != 0 and computer_score < 17:
            computer_hand = deal(cards, computer_hand, 1)
            computer_score = get_total(computer_hand)

    # Print the final scores
    final(player_hand, computer_hand)


# Do you want to play?
while input("Do you want to play blackjack? 'y' or 'n'? ") == 'y':
    system("clear")
    play()
