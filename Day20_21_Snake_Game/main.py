from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = Snake()
food = Food()
score = Score()

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
    
    if snakes.head.distance(food) < 15:
        print("Food collected")
        food.spawn()


screen.exitonclick()