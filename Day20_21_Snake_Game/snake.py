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
        self.head = self.snakes[0]

            
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
        self.head.forward(20)
        
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)