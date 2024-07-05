from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed('fastest')
        self.penup()
        random_x = randint(-280, 280)
        random_y = randint(-280, 250)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)
