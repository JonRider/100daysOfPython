TREASURE = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

DOORS = '''
*******************************************************************************
     __________                 __________                   __________
    |  __  __  |               |  __  __  |                 |  __  __  |
    | |  ||  | |               | |  ||  | |                 | |  ||  | |
    | |  ||  | |               | |  ||  | |                 | |  ||  | |
    | |__||__| |               | |__||__| |                 | |__||__| |
    |  __  __()|               |  __  __()|                 |  __  __()|
    | |  ||  | |               | |  ||  | |                 | |  ||  | |
    | |  ||  | |               | |  ||  | |                 | |  ||  | |
    | |  ||  | |               | |  ||  | |                 | |  ||  | |
    | |  ||  | |               | |  ||  | |                 | |  ||  | |
    | |__||__| |               | |__||__| |                 | |__||__| |
    |__________|               |__________|                 |__________|

*******************************************************************************
'''

SHORE = '''
*******************************************************************************

          |
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
    =- =- -=.--"

*******************************************************************************
'''

import os

print(TREASURE)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are on the inland. To your left is a river to your right you see a desert.")
first = input("Do you go left or right? ").lower()
if first == "left":
    os.system('clear')
    print(SHORE)
    print("You come to a winding river. You see some doors in the sand on the other side.")
    second = input("Do you swim across or wait? ").lower()
    if second == "wait":
        os.system('clear')
        print(DOORS)
        print("Before you on the shore 3 doors appear magically before your eyes. One is red, one is blue and one is yellow.")
        third = input("Which door do you open? ").lower()
        if third == "yellow":
            os.system('clear')
            print(TREASURE)
            print("You open the yellow door. As you do shimmering light bursts forth. Right inside the door is treasure beyound your wildest imagination. You Win!")
        elif third == "blue":
            print("Giant monstrous beasts come barging out of the blue door as you open it. They eat you alive. Game Over.")
        elif third == "red":
            print("You open the red door. Are you stupid? This isn't The Matrix! Flames burst out of the door and roast you alive. Game Over.")
        else:
            print("Well that was stupid. You die. Game Over.")
    else:
        print("You are attacked and eaten by a giant trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
