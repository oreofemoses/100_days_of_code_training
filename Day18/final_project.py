from turtle import Turtle, Screen
from random import choice, random
import colorgram


def color_normalizer(colorgram_colors):
    normalized_colors = []
    for color in colorgram_colors:
        red = color.rgb[0] / 255
        green = color.rgb[1] / 255
        blue = color.rgb[2] / 255
        normalized_colors.append((red, green, blue))
    return normalized_colors


def dotted_lines(turtle, size, length, color_pallet):
    for i in range(length):
        color = choice(color_pallet)
        turtle.dot(size, color)
        turtle.penup()
        turtle.forward(2 * size)
        turtle.pendown()
    turtle.setheading(180)
    turtle.penup()
    turtle.forward(size * length * 2)
    turtle.setheading(90)
    turtle.forward(size * 2)
    turtle.setheading(0)
    turtle.pendown()


colors = colorgram.extract('hrst2.jpg', 20)
norm_colors = color_normalizer(colors)
timmy = Turtle()

timmy.penup()
timmy.hideturtle()
timmy.setheading(205.5)
timmy.forward(250)
timmy.setheading(0)

for i in range(10):
    timmy.speed('fastest')
    dotted_lines(timmy, 20, 10, norm_colors)

screen = Screen()
screen.exitonclick()
