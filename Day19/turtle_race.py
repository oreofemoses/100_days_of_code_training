from turtle import Turtle, Screen
from random import randint


def start():
    colors = ['red', 'blue', 'green', 'yellow', 'orange']
    race_turtles = [Turtle() for i in range(randint(2, 5))]
    y_space = (len(race_turtles) // 2) * 50
    for i in range(len(race_turtles)):
        race_turtles[i].speed("fastest")
        race_turtles[i].color(colors[i])
        race_turtles[i].shape('turtle')
        race_turtles[i].penup()
        race_turtles[i].goto(-screen.window_width() // 2, y_space)
        y_space -= 50
    return race_turtles


def race_alternating_speed(turtles):
    winner = None
    while not winner:
        for turtle in turtles:
            turtle.forward(randint(1, 10))
            if turtle.xcor() >= screen.window_width() // 2:
                winner = turtle
                break
    return winner


def bet_results(bet, winner):
    if bet == winner.fillcolor():
        print(f"{winner.fillcolor()} won the race! continue to cash out!")
    else:
        print(f"{winner.fillcolor()} won the race! You lost.")


#Initialize all we need for the bet

screen = Screen()
screen.setup(width=500, height=500)
user_bet = None
turtles = start()
racing_colors = [turtle.fillcolor() for turtle in turtles]

#Verify that the selected color is in the race.

while user_bet not in racing_colors:
    print(f"{user_bet} is not in this race, choose between: {racing_colors} ")
    user_bet = screen.textinput(title="Bet Window", prompt="Who do you think would win? Enter a color: ").lower()

#Obtain the race results!
race_winner = race_alternating_speed(turtles)
bet_results(bet=user_bet, winner=race_winner)

screen.exitonclick()
