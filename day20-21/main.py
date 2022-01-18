from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

i = 0
segments = []
for _ in range(3):
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.setx(i)
    segments.append(new_segment)
    i -= 20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment_number in range(2, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y = segments[segment_number - 1].ycor()
        segments[segment_number].goto(new_x, new_y)






screen.exitonclick()


