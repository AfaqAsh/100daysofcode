from turtle import Turtle, Screen
import time
from snake import Snake

snake = Turtle()
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = Snake()
screen.listen()

screen.onkey(snakes.turn_up, "Up")
screen.onkey(snakes.turn_left, "Left")
screen.onkey(snakes.turn_down, "Down")
screen.onkey(snakes.turn_right, "Right")

game_off = False

while not game_off:
    screen.update()
    time.sleep(0.1)
    snakes.move()


screen.exitonclick()