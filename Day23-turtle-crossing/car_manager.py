from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    
    
    def __init__(self):
        self.cars = []
        self.create_car()
        self.move_distance = 5
        
        
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len= 2, stretch_wid= 1)
            x_pos = random.randint(280, 350)
            y_pos = random.randint(-280, 280)
            car.goto(x_pos, y_pos)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())
                
    def cars_reset(self):
        self.move_distance += MOVE_INCREMENT