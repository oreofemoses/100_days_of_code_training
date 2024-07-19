from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(x=-290, y=260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align='left', font=FONT)
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align='center', font=FONT)


