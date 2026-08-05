from turtle import Turtle, Screen

all_squares = []
x_posistions = [-20, -40, 0]

for square_index in range(0, 3):
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(x=x_posistions[square_index], y=0)
    all_squares.append(new_square)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Leos Game")



screen.exitonclick()