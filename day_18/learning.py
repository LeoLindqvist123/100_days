import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_col():
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
   random_col = (r, g, b)
   return random_col



directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for i in range(200):
   tim.color(random_col())
   tim.forward(30)
   tim.setheading(random.choice(directions))