from turtle import Turtle
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    
    def __init__(self):
        self.snakes = []
        self.starting_postion = [(0.0,0.0),(-20.0,0.0),(-40.0,0.0)]
        self.create_snake()

            
    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(self.starting_postion[i])
            self.snakes.append(segment)
            
    def move(self):
        for segment in range(len(self.snakes) -1, 0, -1):
            old_coord = self.snakes[segment - 1].pos()
            self.snakes[segment].goto(old_coord)
        self.snakes[0].forward(20)
        
    def turn_up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)
        
    def turn_left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)
        
    def turn_down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)
        
    def turn_right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)