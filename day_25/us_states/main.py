import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct = []

all_state = data.state.to_list()

answer_state = turtle.textinput(title="Guess the State", prompt="What's another state's name?").title()

if answer_state in all_state:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x, state_data.y)
    correct.append(answer_state)
    correct += "1"
