import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game.')
screen.tracer(0)

new_snake = Snake(snake_length=3)
new_food = Food()
sb = Scoreboard()
boundary = [-300, 300]
game_on = True
while game_on:
    screen.listen()
    screen.onkey(key='Up', fun=new_snake.up)
    screen.onkey(key='Down', fun=new_snake.down)
    screen.onkey(key='Left', fun=new_snake.left)
    screen.onkey(key='Right', fun=new_snake.right)
    screen.update()
    time.sleep(0.1)
    new_snake.move()
    if new_snake.head.distance(new_food.pos()) <= 15:  # Test for food collision
        screen.tracer(0)
        new_food.refresh()
        sb.update_score()
        new_snake.grow()
        screen.update()
    if round(new_snake.head.xcor(), 5) in boundary or round(new_snake.head.ycor(), 5) in boundary:  # Beyond boundary
        game_on = False
        sb.game_over(reason="Hit the wall")
    if new_snake.tangle:
        game_on = False
        sb.game_over(reason="Bit Yourself")

screen.exitonclick()
