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

def deal(deck, hand):
    """Deal the requested number of cards to a hand"""
    card = random.choice(deck)
    hand.append(card)
    return hand

def get_total(hand):
    """Get the total value of a hand"""
    total = 0
    for card in hand:
        total += card
    return total

def check_win(player_hand, computer_hand):


from art import logo
import random
# Deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []
# Do you want to play
play = input("Do you want to play blackjack? 'y' or 'n'? ")
if play == "y":
    print(logo)
    # While loop

    # Get starting Cards
    player_hand = deal(cards, player_hand)
    computer_hand = deal(cards, computer_hand)

    # Keep dealing
    dealing = True
    while dealing:
        player_hand = deal(cards, player_hand)
        computer_hand = deal(cards, computer_hand)
        score = get_total(player_hand)
        print(f"    Your cards: {player_hand}, current score: {score}")
        print(f"    Computers first card: {computer_hand[0]}")
        # Check for win
        check_win(player_hand, computer_hand)
        if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
            dealing = False

    # Dealer gets starting Cards
else:
    print("Then get outta here!")

#     Your cards: [3, 10], current score: 13
#     Computers first card: 4
# Type 'y' to get another card, type 'n' to pass:
#     Your final hand: [6, 7, 10], final score: 23
#     Computers final hand: [5, 8, 4], final score: 17
# You went over. You lose (cry)
# Opponent went over. You win (haha)
# You win (happy)
# You lose (angry)
# Lose, opponent has Blackjack (OMG)
# Draw (smile upside down)
# "Do you want to play blackjack? 'y' or 'n'? "
