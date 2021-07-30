# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Set initial bill
bill = 0

# Add cost for Pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Charge for pepperoni based on size
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

# Charge for extra cheese
if extra_cheese == "Y":
    bill += 1

# Print out the final bill
print(f"Your final bill is: ${bill}.")
print("Enjoy your pizza!")
