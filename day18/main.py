from turtle import Turtle, Screen

import heroes

print(heroes.gen())

turtle = Turtle()
# turtle.shape("circle")
# turtle.color("DarkSeaGreen4")

# for _ in range(4):
#     turtle.right(90)
#     turtle.forward(100)

# for _ in range(15):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)

colors = ["DarkRed", "DarkSeaGreen", "blue4", "DarkOrange2", "DarkGoldenrod", "coral2", "aquamarine2", "DarkSalmon",
          "cyan2", "DarkOliveGreen2", "DarkCyan", "DarkMagenta", "DeepPink2", "DeepSkyBlue"]

import random

# i = 3
# for _ in range(7):
#     turtle.color(random.choice(colors))
#     for _ in range(i):
#         turtle.left(360/i)
#         turtle.forward(100)
#     i += 1

# Random Walk
direction = [0, 90, 180, 270]
turtle.pensize(5)
turtle.speed(0)
while True:
    turtle.color(random.choice(colors))
    turtle.right(random.choice(direction))
    turtle.forward(10)

screen = Screen()
screen.screensize()
screen.exitonclick()
