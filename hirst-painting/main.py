# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
colors_list = [(239, 242, 246), (198, 163, 114), (138, 78, 56), (65, 101, 126), (161, 149, 52), (221, 202, 140), (139, 164, 179), (127, 36, 26), (58, 112, 86), (198, 95, 77), (65, 48, 43), (145, 178, 151), (112, 82, 88), (230, 175, 164), (20, 95, 74), (171, 146, 154), (94, 147, 121), (66, 47, 52), (39, 56, 72), (126, 31, 35), (94, 141, 150), (180, 203, 176), (50, 62, 81), (24, 86, 92), (74, 68, 47), (180, 91, 94), (91, 130, 167)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()