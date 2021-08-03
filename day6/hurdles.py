def turn_around():
    repeat(turn_left, 2)

def turn_right():
    repeat(turn_left, 3)

def repeat(function, x):
    for step in range(x):
        function()

def hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        hurdle()
    else:
        move()
