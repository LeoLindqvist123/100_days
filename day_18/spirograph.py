import turtle as t
import random

tim = t.Turtle()
r = 50
t.colormode(255)

def random_col():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   random_col = (r, g, b)
   return random_col

tim.speed("fastest")

def draw_spirograph(size_of_gap):
   for i in range(int(360 // size_of_gap)):
       tim.color(random_col())
       tim.circle(100)
       current_heading = tim.heading()
       tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()    