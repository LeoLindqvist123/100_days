from turtle import Turtle

class Ball(Turtle):
    def __init__(self, posistion):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.shapesize(width= 20, height= 20)
        self.penup()
        self.ycor(0)



    
