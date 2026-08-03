'''
import colorgram 

rgb_colors = []
colors = colorgram.extract("day_18/image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''
import random
import turtle as turtle_module

turtle_module.colormode(255)
leo = turtle_module.Turtle()
leo.speed("fastest")
leo.hideturtle()
leo.penup()
colors_list = [(231, 231, 231), (237, 237, 237), (221, 221, 221), (208, 208, 208), (55, 55, 55), (145, 145, 145), (139, 139, 139), (222, 222, 222), (132, 132, 132), (45, 45, 45), (158, 158, 158), (169, 169, 169), (128, 128, 128), (84, 84, 84), (38, 38, 38), (186, 186, 186), (189, 189, 189), (84, 84, 84), (60, 60, 60), (79, 79, 79), (87, 87, 87), (195, 195, 195), (160, 160, 160), (45, 45, 45), (79, 79, 79), (59, 59, 59), (218, 218, 218), (167, 167, 167)]

leo.setheading(225)
leo.forward(300)
leo.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    leo.dot(20, random.choice(colors_list))
    leo.forward(50)

    if dot_count % 10 == 0:
        leo.setheading(90)
        leo.forward(50)
        leo.setheading(180)
        leo.forward(500)
        leo.setheading(0)
 

screen = turtle_module.Screen()
screen.exitonclick()