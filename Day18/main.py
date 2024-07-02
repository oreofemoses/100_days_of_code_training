import turtle
from turtle import Turtle, Screen
from random import choice, random
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red','blue')
#Challenge 1:
# for i in range(4):
#  timmy.forward(100)
#  timmy.left(90)
#Challege 2:
# for i in range(50):
#  timmy.forward(10)
#  timmy.penup()
#  timmy.forward(10)
#  timmy.pendown()

# Challenge 3:
def draw_shape(sides, turtle, length):
 if sides == 0:
     turtle.circle(length)
 else:
     angles = 360/sides
     for i in range(sides):
      turtle.forward(length)
      turtle.left(angles)
#
# turtle_colors = [
#     "aqua",
#     "coral",
#     "goldenrod",
#     "plum",
#     "chartreuse",
#     "dodger blue",
#     "firebrick",
#     "hot pink",
#     "indigo",
#     "khaki"
# ]
#
# for n in range(3,11):
#  draw_shape(sides=n, turtle=timmy, length=100)
#  timmy.color(choice(turtle_colors))

#Challenge 4

# for i in range(100):
#     color = (random(), random(), random())
#     timmy.color(color)
#     timmy.pensize(10)
#     angle = choice([i * (360 / 10) for i in range(10)])
#     timmy.setheading(angle)
#     timmy.speed('fastest')
#     timmy.forward(50)

#Challenge 5
timmy.speed('fastest')
for i in range(1, 360, 5):
    color = (random(), random(), random())
    timmy.color(color)
    draw_shape(sides=3, turtle=timmy, length=100)
    timmy.setheading(i)

color = (random(), random(), random())
timmy.dot(10, )

















screen = Screen()
screen.exitonclick()


