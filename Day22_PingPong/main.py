from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800,height= 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()

game_off = False

screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")

while not game_off:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    
    if (ball.ycor() > 290 or ball.ycor() < -290):
        ball.bounce()
       
    if (ball.distance(paddle1) < 50 and ball.xcor() > 340) or (ball.distance(paddle2) < 50 and ball.xcor() < -340):
        ball.hit()
        ball.increase_speed()
        
    if ball.xcor() > 390:
        ball.reset_speed()
        ball.reset()
        paddle2.score += 1
        score.update_score(paddle2.score, paddle1.score)

    if ball.xcor() < -390:
        ball.reset()
        paddle1.score +=1
        score.update_score(paddle2.score, paddle1.score)    
screen.exitonclick()