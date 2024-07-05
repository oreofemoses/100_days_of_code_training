from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

#Challenge 1
def move_forward():
    timmy.forward(50)
def move_backward():
    timmy.backward(50)
def rotate_right():
    timmy.right(10)
def rotate_left():
    timmy.left(10)
def clear():
    timmy.home()
    timmy.clear()


screen.listen()
screen.onkey(key='w', fun= move_forward)
screen.onkey(key='s', fun= move_backward)
screen.onkey(key='a', fun= rotate_left)
screen.onkey(key='d', fun= rotate_right)
screen.onkey(key='c', fun=clear)








screen.exitonclick()