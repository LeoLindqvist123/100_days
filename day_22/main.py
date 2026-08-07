from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    
    paddle.goto()

screen.listen()
screen.onkey(go_up, "Up")






screen.exitonclick()
