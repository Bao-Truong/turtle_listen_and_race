import random
from time import sleep
from turtle import Screen, Turtle, textinput

SHAPE = "turtle"
NUMBER_OF_COMPUTERS = 5
SPACE_BETWEEN = 100
WIDTH = (NUMBER_OF_COMPUTERS)*SPACE_BETWEEN
HEIGHT = (NUMBER_OF_COMPUTERS)*SPACE_BETWEEN

screen = Screen()
screen.setup(WIDTH+30, HEIGHT+30)
screen.screensize(WIDTH, HEIGHT)
player_color = screen.textinput(
    title="Make yourbet", prompt="Which turtle will win the race? Enter a color: ")


player = Turtle(SHAPE)
player.color(player_color)
player.penup()

players = [player]
goals = [0 for _ in range(NUMBER_OF_COMPUTERS+1)]


def random_fw(i=0):
    if(i == 0):
        return random.randint(0, 12)
    else:
        return random.randint(1, 10)


def get_color():
    r = random.randint(150, 255)/255
    g = random.randint(150, 255)/255
    b = random.randint(150, 255)/255
    return (r, g, b)


def create_computer(screen):
    global players

    for _ in range(NUMBER_OF_COMPUTERS):
        computer = Turtle(SHAPE)
        computer.color(get_color())
        players.append(computer)


def get_on_position(screen):
    i = 0
    for y in range(-screen.canvwidth//2, screen.canvwidth//2+1, SPACE_BETWEEN):
        computer = players[i]
        computer.penup()
        computer.setpos(-screen.canvwidth//2, y)
        i += 1


def game_start(screen):
    rank = 1
    while(True):
        for i, runner in enumerate(players):
            runner.forward(random_fw(i))
            if(runner.xcor() >= screen.canvwidth//2):
                return i


create_computer(screen)
get_on_position(screen)
winner = game_start(screen)

if(winner == 0):
    print(f"You Win! Player {winner+1} have won")
else:
    print(f"You Lose! Player {winner+1} have won")

screen.exitonclick()
