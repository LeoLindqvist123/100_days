from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(350, 0)

    def r_paddle(self):