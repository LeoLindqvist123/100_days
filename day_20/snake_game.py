from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Leos Game")
screen.tracer(0)

starting_posistions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for posistion in starting_posistions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(posistion)
    segments.append(new_segment)


screen.update()

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)











screen.exitonclick()