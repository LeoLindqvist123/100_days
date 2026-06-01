from turtle import Turtle, Screen


leona_the_turtle = Turtle()
leona_the_turtle.shape("turtle")
leona_the_turtle.color("blue")

for i in range(8):
    leona_the_turtle.forward(100)
    leona_the_turtle.right(90)

screen = Screen()
screen.exitonclick()