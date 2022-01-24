from turtle import Screen, Turtle


timmy = Turtle()


def move_forward():
    timmy.forward(10)


screen = Screen()

screen.listen()
screen.onkey(move_forward, "Up")
screen.exitonclick()
