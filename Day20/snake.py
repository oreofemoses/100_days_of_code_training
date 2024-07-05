from turtle import Turtle


BEGINNING_COORDINATES = (0, 0)
TRAVEL_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, snake_length):
        self.tangle = False
        self.length = snake_length
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        self.snake = [Turtle() for _ in range(self.length)]
        for snake_part in self.snake:
            snake_part.color('white')
            snake_part.shape('square')
            snake_part.penup()
        self.snake[0].fillcolor('green')
        self.snake[0].setposition(BEGINNING_COORDINATES)
        for i in range(1, len(self.snake)):
            self.snake[i].setpos(x=self.snake[i - 1].xcor() - 20, y=0)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setpos(self.snake[i - 1].pos())  # set the position of the i th snake to that of the i-1 snake
        self.head.forward(TRAVEL_DISTANCE)
        self.tangled()

    def tangled(self):
        for segment in self.snake[1:]:
            dist = self.head.distance(segment.pos())
            dist = round(dist, 4)  # Round up for accuracy
            if dist in [0, -0]:  # figured we might have negative zeros, This should help us deal with that
                self.tangle = True
                break

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        snake_part = self.snake[len(self.snake) - 1].clone()
        snake_part.setpos(x=self.snake[len(self.snake) - 1].xcor() + 20, y=self.snake[len(self.snake) - 1].ycor() + 20)
        self.snake.append(snake_part)
