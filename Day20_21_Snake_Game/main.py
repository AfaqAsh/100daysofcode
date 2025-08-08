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
        score.add_score()
        food.spawn()
        snakes.grow()
        
    for segment in snakes.snakes[1:]:
        if snakes.head.distance(segment) < 10:
            game_off = True
            score.game_over()
            snakes.reset_snake()
            
    
    if ((snakes.head.xcor() > 290) or (snakes.head.xcor() < -290) or (snakes.head.ycor() > 290) or (snakes.head.ycor() < -290)):
        # print("game over")
        score.game_over()
        snakes.reset_snake()
        # game_off = True


screen.exitonclick()