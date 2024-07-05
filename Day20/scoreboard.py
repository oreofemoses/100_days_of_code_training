from turtle import Turtle

SCORE = 0
ALIGNMENT = 'center'
FONT = ("Courier", 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.fillcolor('yellow')
        self.penup()
        self.color('white')
        self.setpos(0, 270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, reason):
        self.setpos(0, 0)
        self.write(arg=f"Game Over! you {reason}", align='center', font=("Arial", 25, 'normal'))
