import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
time.sleep(5.0)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()
game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(key='Up', fun=player.move)
    car_manager.create_cars()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect Cross Finish line
    if player.at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()