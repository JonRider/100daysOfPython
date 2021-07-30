# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Combine Names
name = name1 + name2

# Make name lowercase
name = name.lower()

# Initial Score
score1 = 0
score2 = 0

# Check true score (first half of total score)
score1 += name.count("t")
score1 += name.count("r")
score1 += name.count("u")
score1 += name.count("e")

# Check love score (second half of total score)
score2 += name.count("l")
score2 += name.count("o")
score2 += name.count("v")
score2 += name.count("e")

# Final Score
score = int(str(score1) + str(score2))

# Witty Saying
if score > 90 or score < 10:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# name1 = "Angela Yu"
#
# name2 = "Jack Bauer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 53
#
# Print: "Your score is 53."
#
# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.
# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.
