from turtle import Screen
from pongboard import Board
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game.')
screen.tracer(0)

board = Board()

pong_ball = board.ball
screen.update()

max_score = 5
game_on = True
speed = 20
while game_on:
    screen.listen()
    screen.onkey(key='Up', fun=board.right_player.up)
    screen.onkey(key='Down', fun=board.right_player.down)
    screen.onkey(key='w', fun=board.left_player.up)
    screen.onkey(key='s', fun=board.left_player.down)
    pong_ball.move()
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.wall_bounce()

    if 380 < round(pong_ball.xcor(), 5):
        if board.right_player.distance(pong_ball) <= 50:
            pong_ball.player_bounce()
        else:
            board.update_score(side=-1)
            pong_ball.refresh()
    elif round(pong_ball.xcor(), 5) < -380:
        if board.left_player.distance(pong_ball) <= 50:
            pong_ball.player_bounce()
        else:
            board.update_score(side=1)
            pong_ball.refresh()

    if max(board.right_score, board.left_score) == max_score:
        game_on = False
        board.game_over()

    screen.update()
    time.sleep(0.04)

screen.exitonclick()
