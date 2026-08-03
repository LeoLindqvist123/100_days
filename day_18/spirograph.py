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

for i in range(100):
    tim.color(random_col())
    tim.circle(100)
    current_heading = tim.heading()


screen = t.Screen()
screen.exitonclick()    