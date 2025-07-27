from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.penup()
        self.x_disp = 10
        self.y_disp = 10
        
    def move(self):
        new_x = self.xcor() + self.x_disp
        new_y = self.ycor() + self.y_disp
        self.goto(new_x, new_y)
        
    def bounce(self):
        self.y_disp *= -1
        
    def hit(self):
        self.x_disp *= -1
        
    def reset(self):
        # self.clear()
        self.goto(0,0)
        self.x_disp *= -1
        
    def reset_speed(self):
        self.x_disp = 10
        self.y_disp = 10
        
    def increase_speed(self):
        self.x_disp *= 1.2
        self.y_disp *= 1.2