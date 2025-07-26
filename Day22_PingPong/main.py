from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width= 800,height= 800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

game_off = False

screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")

while not game_off:
    screen.update()

screen.exitonclick()