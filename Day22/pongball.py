import random
import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.radius = 0.5
        self.shapesize(stretch_wid=self.radius, stretch_len=self.radius)
        self.speed('slow')
        self.penup()
        self.xspeed = 10
        self.yspeed = 10
        self.refresh()
    def move(self):
        self.goto(self.xcor() + self.xspeed, self.ycor() + self.yspeed)
    def wall_bounce(self):
        self.yspeed *= -1
        self.move()
    def player_bounce(self):
        self.xspeed *= -1
        self.move()
    def refresh(self):
        self.hideturtle()
        time.sleep(0.3)
        self.showturtle()
        self.goto(x=0, y=0)
        self.xspeed *= random.choice([-1, 1])
