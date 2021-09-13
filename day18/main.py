import turtle
import turtle as t
import random

# import heroes
#
# print(heroes.gen())

turtle = t.Turtle()
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

# colors = ["DarkRed", "DarkSeaGreen", "blue4", "DarkOrange2", "DarkGoldenrod", "coral2", "aquamarine2", "DarkSalmon",
#           "cyan2", "DarkOliveGreen2", "DarkCyan", "DarkMagenta", "DeepPink2", "DeepSkyBlue"]
#

# i = 3
# for _ in range(7):
#     turtle.color(random.choice(colors))
#     for _ in range(i):
#         turtle.left(360/i)
#         turtle.forward(100)
#     i += 1

# Random Walk
direction = [0, 90, 180, 270]
turtle.pensize(1)
turtle.speed(0)
t.colormode(255)


def random_color():
    """Generate a random color by returning a tuple with RGB values"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Random Walk
# for _ in range(200):
#     turtle.color(random_color())
#     turtle.setheading(random.choice(direction))
#     turtle.forward(30)

# Spirograph
turtle.home()
degree = 0
while degree < 360:
    turtle.color(random_color())
    turtle.setheading(degree)
    turtle.circle(150)
    degree += 5

screen = t.Screen()
screen.screensize()
screen.exitonclick()
