import turtle as t
import random

tim = t.Turtle()

colours = ["blue", "green", "yellow", "orange", "red", "purple"]
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for i in range(200):
   tim.color(random.choice(colours))
   tim.forward(30)
   tim.setheading(random.choice(directions))