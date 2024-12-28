def turn_right():
    turn_left()
    turn_left()    
    turn_left()
    
def jump():
    turn_left()   
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    turn_right()
    move()
    turn_right()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
done()