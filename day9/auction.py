from art import logo
from os import system

print(logo)
print("Welcome to the blind auction!")

bidders = True
bids = {}

while bidders:
    # Get bidders name and bid
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # Add bidder and bid to dictionary
    bids[name] = bid

    # See if there are more bidders
    again = input("Are there any more bidders, 'yes' or 'no'? ")
    if again == "no":
        bidders = False

    # Clear screen for next bidder
    system("clear")

# Get the higest bid and print out winner
high_bid = 0
high_bidder = ""

for bidder in bids:
    if bids[bidder] > high_bid:
        high_bidder = bidder
        high_bid = bids[bidder]

print(f"{high_bidder} won with a bid of ${bid}.")
