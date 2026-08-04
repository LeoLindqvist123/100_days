from turtle import Turtle, Screen


leona_the_turtle = Turtle()
leona_the_turtle.shape("turtle")
leona_the_turtle.color("blue")
leona_the_turtle.speed("fastest")

def curve():
    for i in range(200):

        leona_the_turtle.right(1)
        leona_the_turtle.forward(1)


def heart():

    leona_the_turtle.fillcolor('red')
    leona_the_turtle.begin_fill()
    leona_the_turtle.left(140)
    leona_the_turtle.forward(113)
    curve()
    leona_the_turtle.left(120)
    curve()
    leona_the_turtle.forward(112)
    leona_the_turtle.end_fill()

# Defining method to write text
def txt():
    
    leona_the_turtle.up()
    leona_the_turtle.setpos(-68, 95)
    leona_the_turtle.down()
    leona_the_turtle.color('lightgreen')

    leona_the_turtle.write("Leona", font=("Verdana", 12, "bold"))

heart()
txt()
leona_the_turtle.ht()
 


screen = Screen()
screen.exitonclick()