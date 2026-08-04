from turtle import Turtle, Screen
import random 


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_posistions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    Leo = Turtle(shape="turtle")
    Leo.color(colors[turtle_index])
    Leo.penup()
    Leo.goto(x=-230, y=y_posistions[turtle_index])



screen.exitonclick()