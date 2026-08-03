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

tim.color(random_col())
tim.speed("fastest")
tim.circle(100)
current_heading = tim.heading()
tim.setheading(current_heading + 10)
tim.circle(100)


screen = t.Screen()
screen.exitonclick()    