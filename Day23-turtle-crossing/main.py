import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
player = Player()
cars = CarManager()


screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()
    cars.move_car()
    
    if player.ycor() > 280:
        score.update_level()
        player.player_reset()
        cars.cars_reset()
        
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()
    
    screen.update()


screen.exitonclick()