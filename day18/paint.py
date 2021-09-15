import colorgram
import turtle as t
import random

NUM_OF_COLORS = 30

extracted = colorgram.extract('painting.jpg', NUM_OF_COLORS)
colors = []
for color in extracted:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    my_color = (r, g, b)
    if not b >= 230:
        colors.append(my_color)

turtle = t.Turtle()
t.colormode(255)
turtle.speed(0)
turtle.penup()
turtle.goto(-220, -220)
turtle.hideturtle()

for _ in range(10):

    for _ in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)

    turtle.goto(-220, turtle.ycor() + 50)

screen = t.Screen()
screen.exitonclick()

