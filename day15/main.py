from menu import MENU


def print_resources(resources_to_print, money):
    """Take available resources and print out the resources formatted"""
    print(f"Water: {resources_to_print['water']}ml")
    print(f"Milk: {resources_to_print['milk']}ml")
    print(f"Coffee: {resources_to_print['coffee']}g")
    print("Money: ${:.2f}".format(money))


def check_resources(ingredients, resources):
    """Check resources available against resources needed and return a message"""
    for item in ingredients:
        if resources[item] < ingredients[item]:
            return f"Sorry there is not enough {item}"
    return "enough"


def insert_coins():
    """Gets inserted coins from the user and returns the total amount in dollars inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return ((quarters * 25) + (dimes * 10) + (nickels * 5) + pennies) / 100


def is_payment_accepted(drink_cost, payment):
    if payment >= drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def serve_drink(ingredients, resources):
    for item in ingredients:
        resources[item] -= ingredients[item]
    return resources


def run_machine():
    """Starts up the coffee machine. Returns 0 on power off"""
    money = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    while True:
        # Prompt user by asking what would you like?
        request = input("What would you like? (espresso/latte/cappuccino): ")
        # Turn off Coffee Machine by entering off to the prompt
        if request == 'off':
            print("Turning off")
            return
        # Print report
        elif request == 'report':
            print_resources(resources, money)
        # Check resources sufficient
        elif request != 'espresso' and request != 'latte' and request != 'cappuccino':
            print("Invalid request. Try again.")
        else:
            drink = MENU[request]
            ingredients = drink['ingredients']
            result = check_resources(ingredients, resources)
            if result != 'enough':
                print(result)
            # Process Coins
            else:
                inserted = insert_coins()
                # Check transaction successful
                drink_cost = drink['cost']
                # Check payment
                if is_payment_accepted(drink_cost, inserted):
                    change = inserted - drink_cost
                    # Give change and make coffee
                    if change == 0:
                        print("Thanks for paying in exact change!")
                    else:
                        print("Here is ${:.2f} in change".format(change))
                    money += drink_cost
                    resources = serve_drink(ingredients, resources)
                    print(f"Here is your {request} ☕. Enjoy!")


run_machine()
