from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

def move_forwards():
    leo.forward(10)

def move_backwards():
    leo.backward(10)

def turn_left():
    new_heading = leo.heading() + 90
    leo.setheading(new_heading)

def turn_right():
    new_heading = leo.heading() - 90
    leo.setheading(new_heading)

    
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.exitonclick()