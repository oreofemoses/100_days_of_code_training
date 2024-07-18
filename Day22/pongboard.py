from turtle import Turtle
from pongplayer import Player
from pongball import Ball

ALIGNMENT = 'center'
FONT = ("Arial", 80, 'normal')


class Board:
    def __init__(self):
        self.printer = None
        self.middle_line = Turtle()
        self.right_score_display = Turtle()
        self.right_score = 0
        self.left_score_display = Turtle()
        self.left_score = 0
        self.divide()
        self.scoreboard(printer=self.right_score_display, score=self.right_score, pos=150)
        self.scoreboard(printer=self.left_score_display, score=self.left_score, pos=-150)
        self.left_player = Player(side=-1)
        self.right_player = Player(side=1)
        self.ball = Ball()
    def divide(self):
        self.middle_line.penup()
        self.middle_line.color('white')
        self.middle_line.setpos(x=0, y=300)
        self.middle_line.setheading(270)
        self.middle_line.pensize(width=3)
        while self.middle_line.ycor() > -300:
            self.middle_line.pendown()
            self.middle_line.forward(10)
            self.middle_line.penup()
            self.middle_line.forward(10)
    @staticmethod
    def scoreboard(printer, score, pos):
        printer.fillcolor('yellow')
        printer.penup()
        printer.color('white')
        printer.setpos(pos, 180)
        printer.write(arg=f"{score}", align=ALIGNMENT, font=FONT)
        printer.hideturtle()
    def game_over(self):
        self.printer = Turtle()
        self.printer.hideturtle()
        self.printer.color('white')
        self.printer.setpos(0, 0)
        self.printer.write(arg=f"Game Over!", align='center', font=("Arial", 30, 'normal'))
    def update_score(self, side):
        if side == 1:
            self.right_score_display.clear()
            self.right_score += 1
            self.right_score_display.write(arg=f"{self.right_score}", align=ALIGNMENT, font=FONT)
        else:
            self.left_score_display.clear()
            self.left_score += 1
            self.left_score_display.write(arg=f"{self.left_score}", align=ALIGNMENT, font=FONT)
