from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    request = input(f"What would you like? ({menu.get_items()})?: ")
    # Turn off Coffee Machine by entering off to the prompt
    if request == 'off':
        print("Turning off")
        is_on = False
    # Print report
    elif request == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
