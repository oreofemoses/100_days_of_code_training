from turtle import Turtle
import math
import random


class ComputerPlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.setpos(x=-305, y=0)

    def track_ball(self, heading):
        if heading < 180:
            while 280 > self.ycor() > -280:
                self.setheading(90)
                self.forward(3)
        elif 180 < heading < 224:
            while 280 > self.ycor() > -280:
                self.setheading(180)
                self.forward(3)
        else:
            self.setpos(x=-305, y=0)


class Player(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapewidth = 4
        self.shapesize(stretch_wid=self.shapewidth, stretch_len=self.shapewidth)
        self.setpos(x=410 * side, y=0)
        self.setheading(90)

    def up(self):
        if 300 >= self.ycor() + 60:
            self.forward(50)
    def down(self):
        if self.ycor() - 60 >= -300:
            self.backward(50)

