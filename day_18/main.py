from turtle import Turtle, Screen


leona_the_turtle = Turtle()
leona_the_turtle.shape("turtle")
leona_the_turtle.color("blue")

for i in range(20):
    leona_the_turtle.forward(10)
    leona_the_turtle.penup()
    leona_the_turtle.forward(10)
    leona_the_turtle.pendown()


screen = Screen()
screen.exitonclick()