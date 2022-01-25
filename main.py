from turtle import Screen, Turtle, distance
from time import sleep
DISTANCE = 10
TURNANGLE = 20

timmy = Turtle()


def move_forward():
    timmy.forward(DISTANCE)


def move_backward():
    timmy.back(DISTANCE)


def turn_left():
    timmy.left(TURNANGLE)


def turn_right():
    timmy.right(TURNANGLE)


def reset():
    timmy.reset()


def turnaround():
    timmy.setheading(180-timmy.heading())


screen = Screen()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(turnaround, "r")
screen.onkey(reset, "c")
screen.exitonclick()
