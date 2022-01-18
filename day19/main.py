from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 400
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.colormode(255)

for i, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, -125 + (i * 50))
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > ((WIDTH / 2) - 20):
            is_race_on = False
            winning_turtle = turtle.pencolor()
            print(f"The {winning_turtle} turtle won!")
            if winning_turtle == user_bet:
                print("You won your bet!")
            else:
                print("You lost your bet!")

# Etch a Sketch Program
# def move_forward():
#     turtle.forward(10)
#
#
# def move_backward():
#     turtle.backward(10)
#
#
# def turn_counter():
#     turtle.left(10)
#
#
# def turn_clockwise():
#     turtle.right(10)
#
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()
#
# # Listen for movement
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_counter, "a")
# screen.onkey(turn_clockwise, "d")
# screen.onkey(clear, "c")


screen.exitonclick()
