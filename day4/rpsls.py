# Rock, Paper, Scissors, Lizard, Spock
# By Jonathan Rider
# Based on the game featured in The Big Bang Theory
# Hail Sam Kass!

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard = """
    _______
---/______ \\
   ///   \_\\_)
   |     / )
   \____/ /
---._____/

"""

spock = '''

        _
       / )
     _/ /
----/  /_____
       _______)
        _______)
       <______
       (______)
---.___(____)

'''

# Imports

# Options Lists
options = [rock, paper, scissors, lizard, spock]
option_names = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# Rules
print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock!\n")
print("*" * 30)
print("Scissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n(and as it always has) Rock crushes Scissors\n")
print("*" * 30)
print("")

# Players Turn
player_choice = -1
while player_choice < 0 or player_choice > 4:
    player_choice = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard or 4 for Spock: "))
print(f"You chose: {option_names[player_choice]}")
print(options[player_choice])

# Computer Turn
computer_choice = random.randint(0, 4)
print(f"The computer chose: {option_names[computer_choice]}")
print(options[computer_choice])

# Test for win
# Lose Cases
if player_choice == 0 and computer_choice == 1:
    print("Paper covers Rock. You Lose!")
elif player_choice == 1 and computer_choice == 2:
    print("Scissors cut Paper. You Lose!")
elif player_choice == 3 and computer_choice == 0:
    print("Rock crushes Lizard. You Lose!")
elif player_choice == 4 and computer_choice == 3:
    print("Lizard poisons Spock. You Lose!")
elif player_choice == 2 and computer_choice == 0:
    print("Rock crushes Scissors. You Lose!")
elif player_choice == 2 and computer_choice == 4:
    print("Spock smashes Scissors. You Lose!")
elif player_choice == 3 and computer_choice == 2:
    print("Scissors decapitates Lizard. You Lose!")
elif player_choice == 1 and computer_choice == 3:
    print("Lizard eats Paper. You Lose!")
elif player_choice == 4 and computer_choice == 1:
    print("Paper disproves Spock. You Lose!")
elif player_choice == 0 and computer_choice == 4:
    print("Spock vaporizes Rock. You Lose!")

# Win Cases
elif player_choice == 1 and computer_choice == 0:
    print("Paper covers Rock. You Win!")
elif player_choice == 2 and computer_choice == 1:
    print("Scissors cut Paper. You Win!")
elif player_choice == 0 and computer_choice == 3:
    print("Rock crushes Lizard. You Win!")
elif player_choice == 3 and computer_choice == 4:
    print("Lizard poisons Spock. You Win!")
elif player_choice == 0 and computer_choice == 2:
    print("Rock crushes Scissors. You Win!")
elif player_choice == 4 and computer_choice == 2:
    print("Spock smashes Scissors. You Win!")
elif player_choice == 2 and computer_choice == 3:
    print("Scissors decapitates Lizard. You Win!")
elif player_choice == 3 and computer_choice == 1:
    print("Lizard eats Paper. You Win!")
elif player_choice == 1 and computer_choice == 4:
    print("Paper disproves Spock. You Win!")
elif player_choice == 4 and computer_choice == 0:
    print("Spock vaporizes Rock. You Win!")

# Tie Cases
else:
    print(
        f"{option_names[player_choice]} and {option_names[computer_choice]}. It's a tie.")
