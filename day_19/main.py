from turtle import Turtle, Screen
import turtle as t
import random

leo = Turtle()
screen = Screen()
leo.shape("turtle")
t.colormode(255)

def random_color():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   random_col = (r, g, b)
   return random_color

def move_forwards():
    leo.forward(10)
    leo.color(random_color)

    
def move_backwards():
    leo.backward(10)
    leo.color(random_color)

def turn_left():
    new_heading = leo.heading() + 90
    leo.setheading(new_heading)
    leo.color(random_color)

def turn_right():
    new_heading = leo.heading() - 90
    leo.setheading(new_heading)
    leo.color(random_color)

def reset():
    leo.reset()
    
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="l", fun=reset)
screen.exitonclick()