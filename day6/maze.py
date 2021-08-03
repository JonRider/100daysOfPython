def turn_right():
    repeat(turn_left, 3)

def repeat(function, x):
    for step in range(x):
        function()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
