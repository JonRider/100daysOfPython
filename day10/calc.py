from art import logo
from os import system

# Calculator Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Operations Dictionary
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)
    a = float(input("What's the first number?: "))
    while True:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        b = float(input("What's the second number?: "))
        # Calculate the result using the given operator
        function = operations[operator]
        result = function(a, b)
        print(f"{a} {operator} {b} = {result}")
        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        # Clear the screen and run again
        if again == 'n':
            system("clear")
            calculator()
        else:
            # Set a equal to current result
            a = result

# Run program on start
calculator()
